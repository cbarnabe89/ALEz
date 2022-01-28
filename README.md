# ALEz
Final Solo Project for CD
My project is for a real world application.
I work in the insurance industry and find a lot of tasks could be automated.
Using a combination of HTML, CSS, JS and Python w/Flask, I will build a web app that puts the creation of an "ALE Worksheet" into the hands of both the insured and the claim representative.

The aim of the app is to actually focus on the insured.
I would consider this more like freeware for them to use to keep a record of their own expenses, which can also be given to the claim rep for adjusting - rather than have it built out to be more towards the claim representative who then oversees more workload - it would end up another thing for the claim rep to keep track of and we actually want to get rid of that.

MVP Feature List:
-Unique Login and Registration.
-Many claims are able to be registered/created under 1 user.
-Calculator does all the math for you once you put in the values.
-Users can update the file themselves as they incur more expenses.
-Users can view/read and print a PDF of the completed Worksheet.
-Users can delete a worksheet if they decide to no longer pursue the claim.

Future Feature List:
-more itemized version of the app-not just totals but each individual receipt amount that makes up those totals could be added and accessed. This could also substantially change how the app looks and behaves. 
-upload a picture of the receipt. Have these all print as part of the PDF.
-Include the date of the individual receipt when uploading and validate it against the date of loss.
-Make it more mobile friendly (current version has big long forms - maybe break down by subcategory).

Worksheet validations include: claim number must be longer than 2 characters, date of loss must be input, if additional food expense is entered into the form, but no normal expense is entered it throws a validation error, if total ALE claim is == 0, and if the total ALE claim is less than zero it throws a validation error.

User validation is first name and last name must be longer than 2 characters, password must be at least 8 characters, password confirmation must match first pass on password, email must be unique, valid email address must be present. 
