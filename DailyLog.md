## Week 1: First Week 

<br />

### August 30, 2021 (Day 1)

Updates:
* Finished Day 1 of orientation.
* Resubmitted all forms from this past summer.
* Registered for an account with APS.

<br />

### August 31, 2021 (Day 2)

Updates:
* Finished Day 2 of orientation.

<br />

### September 1, 2021 (Day 3)

Updates:
* Was able to access https://delos.aps.anl.gov/nxwebplayer for virtual workstation.
* Met with Dr. Qingteng Zhang to discuss goals and guidelines for project.

* To Do:
* Dr. Zhang sent me some [readings](https://drive.google.com/drive/folders/1sbOvnYCbVQB4D0wJcitgfYjVvuzybM8h?usp=sharing) for the project. Will get to those tomorrow.

<br />

### September 2, 2021 (Day 4)

Updates:
* Read the papers/slides.
* Did a demo with the MatLab GUI following the instructions on Data FlowChart PPT.
* Cloned Git Repos for simple_mask onto local desktop.
* Met with group members in group meeting. 

<br />

### September 3, 2021 (Day 5)
Updates:
* Met with group members in software development meeting.
* Was able to have simple_mask program running with the help of quick fixes. 
* Reference: 
    1) [Can't install PyQt5 on python 3 with spyder ide](https://stackoverflow.com/questions/62980464/cant-install-pyqt5-on-python-3-with-spyder-ide).
* Cloned pyxpcs.
* Watching/Reading PyQt tutorials suggested by Dr. Miaoqi Chu.
* References: 
    1) [The complete PyQt5 & PyQt6 tutorial — Create GUI applications with Python](https://www.pythonguis.com/pyqt-tutorial/)
    2) [Welcome to the documentation for pyqtgraph](https://pyqtgraph.readthedocs.io/en/latest/)

<br />



## Week 2: 

<br />

### September 7, 2021 (Day 6)
Updates:
* Completed some forms from Orientation. Finished pre-Internship survey on WTDS.
* Attended meeting with QZ, Miaoqi, Faisal to discuss on this week's assignment. Will be working on data reading functions that we can incorporate on to the Python GUI.
* QZ uploaded data files from detectors, Rigaku and Lambda to Box. Files are large, so I will not upload on GitHub or Google Drive. 
* Was able to read .bin file with xpcs program. However, I was not able to plot the image properly using MatplotLib. The goal is to have the plot resemble what is presented using the MatLab GUI.   

Goals for this week:
* Understand modules in program.
* Learn how to use PyQt.
* Ask questions.

<br />

### September 8, 2021 (Day 7)
Updates:
* I was not able to install MatLab because my Emory license expired. That is ok, because I still have access to remote server. 
* Talked with QZ on how to properly plot the figures. We played around with scaling of the plot using log10 and lognorm. For log10, the matrix values were all operated with log10. For lognorm, it was more complicated and an explanation can be found on the Matplotlib [document](https://matplotlib.org/stable/tutorials/colors/colormapnorms.html). 
* I uploaded the program and the plots on Google Drive. The results can be found [here](). Comparing the results, we see that log10 leaves a lot of white space, but this was easily corrected using lognorm scaling. 

<br />

### September 9, 2021 (Day 8)
Updates:
* Worked on running the imm method, making sure it can accept and read .imm files properly. 
* Was able to have the program output index and numnbers. Both of these are lists containing numpy arrays. I uploaded the program and the plots on Google Drive. The results can be found [here]().
* QZ showed me a tour of the beamline inside Argonne using his lens software. I thought it was very cool. Allowed me to understand a bit better on what I am doing and how my work will be relevant. 
* Attended brief APS Orientation about safety.

<br />

### September 10, 2021 (Day 9)
Updates:
* Attended software development group meeting. Presented my updates and asked questions regarding upcoming project. 
* The main question I had is why the outputs for Rigaku and IMM were different. IMM is a lot older technology, collecting one frame per second. The possibiltiy of collecting 0 photons in one frame was very very slim. On the other hand, Rigaku collects 15000 frames per second. The possibility of collecting 0 photos in one frame is a lot higher and more often. Thus, the index is outputted for Rigaku.
* Worked on developing a function that plots IMM data, given the index data and value data. 
* Looked into existing Git repos by Faisal to see what was previously done. Was unsure on how to 

<br />



## Week 3: 

<br />

### September 10, 2021 (Day 9)
Updates:

<!-- ## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6 -->
