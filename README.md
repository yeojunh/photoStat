# Photo Stat 
## About the Project
PhotoStat is intended to be a web-based AI to solve introductory hypothesis tests (z-tests and t-tests of Normal distributions) by inserting an image of a word problem or typing out the question. 

This project is a work in progress. I will first implement the project _without_ using AI. I will extract necessary data from the word problem using other methods for the initial implementation of the project. Then, I will re-implement the project using AI.

## Functionalities:
- Website with a simple interface to take/insert an image of a word problem or type out the question
- Option to take a picture of the word problem
- Option to upload a picture of the word problem
- Option to type out the word problem
- Allow users to view a step-by-step process of the hypothesis test
- Option to copy the solution to the clipboard or save it to a file
- ~~View more information about the AI regarding its reliability (%) and the project~~


## Tasks
- [x] Add a way to process the image into text 
- [ ] Refine image to text processing accuracy 
- [ ] ~~Train a model to extract core data (e.g. mean, standard deviation, etc.) from the problem~~
- [ ] ~~Train a model to perform the hypothesis test~~
- [ ] ~~Train a model to differentiate between z-tests and t-tests~~
- [ ] Allow users to view a step-by-step process of the hypothesis test
- [ ] Allow users to copy the solution to the clipboard
- [ ] Allow users to save the solution to a file
- [ ] Allow users to share the solution with others
- [ ] Create a website for the project
- [ ] ~~Connect the AI to the website~~
- [ ] ~~Allow users to view more information about the AI regarding its reliability (%) and the project~~
- [ ] Create a histogram of the website's daily/weekly/monthly usage and save it to a spreadsheet 

## Built With 
- [Pytesseract](https://pypi.org/project/pytesseract/)
    - You will need to install: 
        -  ```pip install pytesseract```
        - [Download Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)

## References 
- [Image to Text](https://www.youtube.com/watch?v=4DrCIVS5U3Y)