Hi All,
This is very simple basic script to connect SharePoint List and creates an item in list. 

Purpose to do script: 
To automate ticket creation process on SharePoint which is received on outlook to a GAL using SharePoint API by Microsoft.

Design Approach: 
We are operating as L2 team for one of our application and some tickets need to be escalated with L3 team for further analysis and issue troubleshooting. So, We used to create ticket manually filling all values and then sending ticket to L3 team for further processing. 
And this tickets which we need to forward to L3 team, that form is having standard values or default values so some of fields can be set already usning variables. so this is how we decided to automate the ticket creation process.
The list item is actually you could say is a form with various values which we have decided and configured as per our app/task requirement. All in all this is basic overview behind all this mess you could say.

Implementation:
So when we started with this automation approach we were not having idea of how we gonna do this & execute but we have fixed the language used will be Python. 
Now why Python: 
  a. Some backgorund or familiarity with language
  b. Widely used & supported by various platforms
  c. Various in-built libraries & modules are readily available 
  d. To try to learn with new tools, libraries.
with some of this advantages we choose it. 
Our process has 3 tasks that we divided:
  1. Connect first with mail account & log in with credentials. 
  2. Check whether the ticket has been raised(needs to be escalate the issue or if there is already case linked to it or if it's fresh ticket); as our L3 team works every time on fresh tickets.
  3. Connect with SharePoint account & get access to list.
  4. Create ticket with details provided in mail.
  5. Share the ticket ID with concern stakeholders on mail to L3 team notifying of ticket created with ID. 
  
You can also find piece of code for each of above mentioned tasks/process below for reference:
                               





  
  
  
