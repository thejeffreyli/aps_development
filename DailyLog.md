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
* Talked with QZ on how to properly plot the figures. We played around with scaling of the colormap using log10 and lognorm. For log10, the matrix values were all operated with log10. For lognorm, it was more complicated and an explanation can be found on the Matplotlib [document](https://matplotlib.org/stable/tutorials/colors/colormapnorms.html). 
* More background on colormap normalization: Objects that use colormaps by default linearly map the colors in the colormap from data values vmin to vmax. Matplotlib does this mapping in two steps, with a normalization from the input data to [0, 1] occurring first, and then mapping onto the indices in the colormap. However, there are sometimes cases where it is useful to map data to colormaps in a non-linear fashion.
* I uploaded the plots on Google Drive. The results can be found [here](https://drive.google.com/drive/folders/1Lu-8x097JKolMsWuReA4etekUZVenEoY?usp=sharing). Comparing the results, we see that log10 leaves a lot of white space, but this was easily corrected using lognorm scaling. This transformation is useful to display changes across disparate scales. Using colors.LogNorm normalizes the data via log10.
* The Git repo for the Rigaku code can be found [here](https://github.com/thejeffreyli/suli_fall_2021/blob/main/Week_02/rigaku_reader.py).

<br />

### September 9, 2021 (Day 8)
Updates:
* Worked on running the .imm method, making sure it can accept and read .imm files properly. Moreover, the program outputs two parameters, index and value. Both of these are in the form of lists containing numpy arrays and will be important for the plotting of the XPCS data.
* The Git repo for the Rigaku code can be found [here](https://github.com/thejeffreyli/suli_fall_2021/blob/main/Week_02/imm_reader.py).
* QZ showed me a tour of the beamline inside Argonne using his lens software. I thought it was very cool, and it allowed me to understand better on what I am doing and the relevancy of my work. 
* Attended brief APS Orientation about safety.

<br />

### September 10, 2021 (Day 9)
Updates:
* Attended software development group meeting. Presented my updates and asked questions regarding upcoming project. 
* The main question I had is why the outputs for Rigaku and IMM were different. IMM is a lot older technology, collecting one frame per second. The possibiltiy of collecting 0 photons in one frame was very, very slim. On the other hand, Rigaku collects 15000 frames per second. The possibility of collecting 0 photos in one frame is a lot higher and more frequent. Thus, 'index' is an additional parameter for Rigaku that is not found in IMM's output. 
* Worked on developing a function that plots .IMM files, given the index data and value data. Looked into existing Git repos by Faisal to see what was previously done. 
* References: 
    1) [corr.cpp](https://github.com/pyxpcs/pyxpcs/blob/master/src/libpyxpcs/corr.cpp)
    2) [viz.py](https://github.com/pyxpcs/pyxpcs/blob/master/src/pyxpcs/viz.py)
    3) [XPCS Analysis IMM](https://github.com/thejeffreyli/suli_fall_2021/blob/main/Week_02/XPCS%20Analysis%20IMM.html)


<br />



## Week 3: 

<br />

### September 13, 2021 (Day 10)
Updates:
* Had difficulties with plotting figures since I was unfamiliar with the sparse technique.
* Spoke with Faisal and he guided me towards the right direction. I did not need to use the sparse matrix technique, since it would be more computationally intensive and the goal was not to calculate but to only  create a graphical depiction.
* Made some additions to the .IMM reader. 
* The Git repo for the Rigaku code can be found [here](https://github.com/thejeffreyli/suli_fall_2021/blob/main/Week_02/rigaku_reader.py). The plots can be found on the Google Drive [here]().

<br />

### September 14, 2021 (Day 11)
Updates:
* Had difficulties 

<br />

### September 15, 2021 (Day 12)
Updates:
* Had difficulties 

<br />

### September 16, 2021 (Day 13)
Updates:
* Had difficulties 

<br />

### September 17, 2021 (Day 14)
Updates:
* Had difficulties 

<!-- ## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6 -->
