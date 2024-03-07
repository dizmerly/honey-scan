# Honey Scan

This is a project creating a tool that scans groceries as they are put into the fridge.
It was inspired by the barcode scanning functionality of the app MyFitnessPal. The goal is to create something
that is convenient for the user to keep track of what they have in their fridge, while keeping it at an affordable price
compared to smart fridges that have similar technology, but are priced at thousands of dollars.


![Drawing](images/Drawing.png)



![image 1](images/modelAngle.png)


![image 2](images/modelTopDown.png)


The python code that the project revolves around is a script that sends requests to 
Google's Gemini Vision API. 

```commandline
    resp = requests.post(
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent?key=' + API_TOKEN,
        json=query)
```


The case for the raspberry pi is built using a 3D printer. 

![3dPrint](images/3dprint.jpeg)