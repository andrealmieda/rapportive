# Rapportive

Rapportive is an Chrome extension that permites the visualization of the Linked In Profiles in your Gmail Webpage

The objective of this app is to generate all to possible combinations of first name and last name to create an email address in a specific company domain, as demonstrated [here](http://dis.tl/name2email) and find with of those email are valid.

## Problems

Recently Rapportive, changed their api configuration and one of the possible ways ([Jordan Wright](https://github.com/jordan-wright/rapportive)), was no longer possible, so after some search and exploring, I found a possible way to "make it work, again".

The new Rapportive chrome extension uses a iframe to get the **li_at** cookie that will be used to get the **OAuth** key needed to use the email-search API.

If the Chrome user doesn't have an active session in the Linked In website, the extension won't work.

So for the app to work we will need the value of the **li_at** cookie. Right now this value is hardcoded for the application to work, in Django Settings (seedstars_challenge/settings.py).

## Usage

1. Create a virtual env
2. Install Django
3. git clone https://github.com/andrealmieda/rapportive.git
4. Go to your Chrome Cookies and copy the value of the li_at cookie from the Linked In Domain
5. Paste the value in to the **LI_AT** variable in to the settings.py file
6. Run the django server
