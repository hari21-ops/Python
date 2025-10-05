First 4 steps will be same as scriptOne.py, like logging in to account, using username and cred to create ticket. 
After that will writing logic for secondScript.py: 
def get_form_digest():
    url = f"{site_url}/_api/contextinfo"
    response = requests.post(url, headers={"Accept": "application/json;odata=verbose"},
                             auth=HttpNtlmAuth(username, password), verify=False)
    if response.status_code == 200:
        return response.json()['d']['GetContextWebInformation']['FormDigestValue']
    logging.error("❌ Failed to get form digest.")
    return None

def get_entity_type():
    url = f"{site_url}/_api/web/lists/getbytitle('{list_name}')?$select=ListItemEntityTypeFullName"
    response = requests.get(url, headers={"Accept": "application/json;odata=verbose"},
                            auth=HttpNtlmAuth(username, password), verify=False)
    if response.status_code == 200:
        return response.json()['d']['ListItemEntityTypeFullName']
    logging.error("❌ Failed to get list entity type.")
    return None

def get_pending_items():
    url = f"{site_url}/_api/web/lists/getbytitle('{list_name}')/items?$filter=SR_x0020_Status eq 'TC L3 Assignment Pending'"
    response = requests.get(url, headers={"Accept": "application/json;odata=verbose"},
                            auth=HttpNtlmAuth(username, password), verify=False)
    if response.status_code == 200:
        return response.json()['d']['results']
    logging.error("❌ Failed to fetch items from SharePoint.")
    return []

def update_item(item_id, updates, digest, entity_type):
    url = f"{site_url}/_api/web/lists/getbytitle('{list_name}')/items({item_id})"
    headers = {
        "Accept": "application/json;odata=verbose",
        "Content-Type": "application/json;odata=verbose",
        "X-RequestDigest": digest,
        "IF-MATCH": "*",
        "X-HTTP-Method": "MERGE"
    }
    body = {
        "__metadata": {"type": entity_type},
        **updates
    }
    response = requests.post(url, headers=headers, auth=HttpNtlmAuth(username, password),
                             data=json.dumps(body), verify=False)
    return response.status_code in [200, 204]

# ---- Excel Roster Assignment ----
def get_assigned_user_id():
    try:
        df = pd.read_excel(EXCEL_PATH, header=None)
        date_row = pd.to_datetime(df.iloc[1, 1:], errors='coerce').dt.date
        today = datetime.now().date()

        if today not in date_row.values:
            logging.warning("⚠️ Today's date not found in roster. Using fallback.")
            return DEFAULT_ASSIGNEE

        col_index = date_row[date_row == today].index[0]
        names = df.iloc[2:, 0]
        availability = df.iloc[2:, col_index]

        for name, val in zip(names, availability):
            if str(val).strip().upper() == 'Y':
                base_email = str(name).strip().lower().replace(" ", "")
                if '@' not in base_email:
                    base_email += '@ril.com'
                return email_to_spid.get(base_email, DEFAULT_ASSIGNEE)

        logging.warning("⚠️ No one is available today in the roster. Using fallback.")
        return DEFAULT_ASSIGNEE

    except Exception as e:
        logging.error(f"❌ Error reading roster: {e}")
        return DEFAULT_ASSIGNEE

# ---- Main Execution ----
def main():
    digest = get_form_digest()
    if not digest:
        return

    entity_type = get_entity_type()
    if not entity_type:
        return

    items = get_pending_items()
    if not items:
        logging.info("✅ No 'TC L3 Assignment Pending' items found.")
        return

    assigned_to_id = get_assigned_user_id()

    for item in items:
        item_id = item['Id']
        im_number = item.get('HPSM_x0020_IM_x0020_Number', 'UNKNOWN')
        current_notes = item.get('SR_x0020_Updates_x0020__x002d__x', '') or ''
        updated_notes = current_notes + "\n\nUpdate 2: L3 assignment done"

        update_data = {
            'SR_x0020_Status': "TC L3 Assigned",
            'SR_x0020_Updates_x0020__x002d__x': updated_notes,
            'Assigned_x0020_ToId': assigned_to_id
        }

        success = update_item(item_id, update_data, digest, entity_type)
        if success:
            logging.info(f"✅ Updated IM {im_number} (Item ID: {item_id})")
        else:
            logging.error(f"❌ Failed to update IM {im_number} (Item ID: {item_id})")

if __name__ == "__main__":
    main()
