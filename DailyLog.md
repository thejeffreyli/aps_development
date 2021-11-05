## Week 1: First Week 

<br />

### August 30, 2021 (Day 1)
Updates:
* Finished Day 1 of orientation.
* Resubmitted all required forms, luckily most were completed during my Summer SULI term.
* Registered for an account with APS.

<br />

### August 31, 2021 (Day 2)
Updates:
* Finished Day 2 of orientation.

<br />

### September 1, 2021 (Day 3)
Updates:
* Was able to access https://delos.aps.anl.gov/nxwebplayer for virtual workstation.
* Met with Dr. Qingteng Zhang (QZ) to discuss goals and guidelines for project.
* To Do:
* Dr. Zhang sent me some [readings](https://drive.google.com/drive/folders/1sbOvnYCbVQB4D0wJcitgfYjVvuzybM8h?usp=sharing) for the project. Will get to those tomorrow.

<br />

### September 2, 2021 (Day 4)

Updates:
* Read the papers/slides.
* Did a demo with the MatLab GUI following the instructions on Data FlowChart PPT (from readings).
* Cloned Git Repos for simple_mask onto local desktop. This is the GUI I will be working on during my internship term.
* Met with group members in group safety meeting. 

<br />

### September 3, 2021 (Day 5)
Updates:
* Met with group members in software development meeting.
* Was able to have simple_mask program running with the help of minor fixes. 
* Reference: 
    1) [Can't install PyQt5 on python 3 with spyder ide](https://stackoverflow.com/questions/62980464/cant-install-pyqt5-on-python-3-with-spyder-ide).
* Cloned pyxpcs.
* Watching/Reading PyQt tutorials suggested by Dr. Miaoqi Chu.
* References: 
    1) [The complete PyQt5 & PyQt6 tutorial — Create GUI applications with Python](https://www.pythonguis.com/pyqt-tutorial/)
    2) [Welcome to the documentation for pyqtgraph](https://pyqtgraph.readthedocs.io/en/latest/)

<br />



## Week 2: Reading and Plotting Rigaku (.bin), Lambda (.imm)

<br />

### September 7, 2021 (Day 6)
Updates:
* Completed some forms from Orientation. Finished pre-Internship survey on WTDS.
* Attended Student Connects meeting.
* Attended meeting with QZ, Miaoqi, Faisal to discuss on this week's assignment. Will be working on data reading functions that we can incorporate on to the Python GUI.
* QZ uploaded data files from detectors, Rigaku (.bin) and Lambda (.imm) to Box. Files are large, so I probably will not upload on GitHub or Google Drive. 
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
* The Git repo for the Rigaku code can be found [here](https://github.com/thejeffreyli/suli_fall_2021/blob/main/progress/Week_02/rigaku_reader.py).

<br />

### September 9, 2021 (Day 8)
Updates:
* Worked on running the .imm method, making sure it can accept and read .imm files properly. Moreover, the program outputs two parameters, index and value. Both of these are in the form of lists containing numpy arrays and will be important for the plotting of the XPCS data.
* The Git repo for the .IMM code can be found [here](https://github.com/thejeffreyli/suli_fall_2021/blob/main/progress/Week_02/imm_reader.py).
* QZ showed me a tour of the beamline inside Argonne using his lens software. I thought it was very cool, and it allowed me to understand better on what I am doing and the relevancy of my work for the APS division.
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



## Week 3: Reading and Plotting Lambda (.imm), Reading Metadata (HDF)

<br />

### September 13, 2021 (Day 10)
Updates:
* Had difficulties with plotting figures since I was unfamiliar with the sparse technique.
* Spoke with Faisal and he guided me towards the right direction. I did not need to use the sparse matrix technique, since it would be more computationally intensive and the goal was not to calculate but to only create a graphical depiction.
* Made some additions to the .IMM reader. 
* The Git repo for the revised .IMM plotter can be found [here](https://github.com/thejeffreyli/suli_fall_2021/blob/main/progress/Week_02/imm_reader_with_plot.py). The plots can be found on the Google Drive [here](https://drive.google.com/drive/folders/1lhwqcgPCY3ucNjv0RSdv9Q6jHWoMHED_?usp=sharing). The familiar circular shape can be seen in these plots. 

<br />

### September 14, 2021 (Day 11)
Updates:
* Attended Student Connects meeting.
* Attended meeting with QZ and Miaoqi to discuss on this week's assignments. Need to make some minor adjustments to the plots; rather than plotting a single frame, I should plot the average sum. Moreover, some other things I should incorporate include:
    1) Function that reads and extracts parameters from .HDF file.
    2) Function that parses exisiting directory for .IMM/.BIN file.
    3) Function that calls on appropriate plotting/reader function for either .IMM or .BIN.
* Talked with QZ about graduate school and his experiences. 

<br />

### September 15, 2021 (Day 12)
Updates:
* Looked into ways for searching through existing directories. [Source](https://www.geeksforgeeks.org/file-searching-using-python/)
* Developed program that follows the requirements mentioned yesterday. In short, given a .HDF file, the program is able to extract the necessary parameters for the GUI. Then it can find exisiting .IMM or .BIN files in its directory. Next, it will generate plots of the file using respective reading and plotting methods already developed from Week 2 and 3. 
* The Git repo for the program can be found [here](https://github.com/thejeffreyli/suli_fall_2021/blob/main/progress/Week_03/hdf_extractor.py). The results can be found on the Google Drive [here](https://drive.google.com/drive/folders/1anDBwaMMTmvfzQJtk7o1LA7paIKfZbrd?usp=sharing). 

<br />

### September 16, 2021 (Day 13)
Updates:
* Started implementing the hdf_extractor.py program into the existing GUI. This would be done as a function inside simple_mask_kernel The main goal for now is to have the plot be properly displayed in the GUI viewer and data be read from the hdf file. 
* Encountered bugs upon startup of program due to some parameters that seem to be missing. Plots would not load, deduced issue to being that matplotlib is not needed in my function since it is being called elsewhere. 
* Attended group safety meeting. 

<br />

### September 17, 2021 (Day 14)
Updates:
* Miaoqi clarified the issues I was having yesterday. Firstly, I was encountering bugs, because I was not loading the saxs file properly. The saxs file is required for the plot, because it is what needs to be read by a plotting function. Secondly, both the outputs of the file_search function should be 2D arrays. This is the accepted form for the program. 
* I overcame the bugs due to Miaoqi's tips. I had to comment out a section of Miaoqi's program that gave formatting errors.
* The plots came out nicely, and can be found [here](https://drive.google.com/drive/folders/1ssuXm_m3gZ6aqssq61IrAv9ZYR5tq_gr?usp=sharing). 
* Downloaded HDF Viewer for Windows.

<br />


## Week 4: Formatting QMap (.H5) Results

<br />


### September 20, 2021 (Day 15)
Updates:
* QZ wanted me to write the parameters/data from the program into a qmap (.h5) file. 
* Read more into what a .h5 file is and how I can write the file using Python.
* Sources: 
    1) [HDF5 for Python](https://docs.h5py.org/en/latest/index.html) 
    2) [HDF5 files in Python](https://www.geeksforgeeks.org/hdf5-files-in-python/)
* Used HDF viewer to examine content of 'jaeger202106_Lq0_S360_D36' h5 file. My goal was to create a program that generates the directories present in the jaeger qmap file.
* Noticed most of the parameters/data could not be found (or were not easily found) from Miaoqi's code. Asked QZ if we can talk more about this tomorrow during the meeting.


### September 21, 2021 (Day 16)
Updates:
* Attended Student Connects meeting.
* Met with QZ and Miaoqi to discuss updates to the program. We made an excel spreadsheet that describes the directories inside the qmap file, what each data means, and where/how to potentially extract them using the simple_mask GUI. 
* The spreadsheet can be found [here](https://drive.google.com/drive/folders/15-8h7e3sxLXSJINYhrL2zwGVaTEEpWEO?usp=sharing).

### September 22, 2021 (Day 17)
Updates:
* Worked on developing a function capable of extracting the necessary values (calculated and read) from the program. 
* Finished a majority of them. Could not find /data/Maps/x and /data/Maps/y in maps. /data/dphival and /data/sphival provide data types different than ones shown in 'jaeger.'
* Diagram of algorithm can be found [here](https://drive.google.com/drive/folders/1WV2Y7s7QGoZe7FGNvRFErvPVHWVwP8gT?usp=sharing).

### September 23, 2021 (Day 18)
Updates:
* Finished developing function. Sample qmap results can be found [here](https://drive.google.com/drive/folders/1NY722D6_cf_Gtd-iovFPk5sqRFdp9JK7?usp=sharing).
* Worked on presentation for tomorrow's meeting. Presentation can be found [here](https://drive.google.com/drive/folders/10VWe26YWnG1oSzGqIlN6rkc40vDsIc8I?usp=sharing).
* Prepared questions about graduate school, so I can ask the APS faculty in meeting tomorrow.


### September 24, 2021 (Day 19)
Updates:
* Presented updates in meeting. 
* Scheduled meeting with Mr. Nicholas Schwarz for career advice next week.
* QZ has to test .h5 files on his end. No updates.

<br />


## Week 5: Improving General GUI Functions/Conditions

<br />

### September 27, 2021 (Day 20)
Updates:
* QZ has to test .h5 files on his end. No updates.

<br />

### September 28, 2021 (Day 21)
Updates:
* Attended Student Connects meeting.
* Met with QZ and Miaoqi to discuss updates to the program. 
* QZ experienced errors with my program since the results deviated from what was shown in the IMM JN by Faisal. He suspects errors can be improved through implementing a mask.
* To do: 
    1) Read mask array from new file titled cluster_result > H432_OH_100_025C_att05_001_0001-1000.hdf.
    2) Use mask array and generate a new qmap. Give QZ the new qmap.
    3) Draw a circle using GUI. 
    4) Generate another qmap using the new mask. 
* Miaoqi was going to develop new function for readng hdf5 raw data file. Hdf5 file is raw data (from detector), not to be confused with hdf file which is meta data. The goal for this would be to read files from yuyin202109.

<br />

### September 29, 2021 (Day 22)
Updates:
* Miaoqi sent out new function last night, it can be found [here](https://github.com/thejeffreyli/suli_fall_2021/blob/main/progress/Week_05/hdf2sax.py). I incorporated it as a test function, but was unable to read the files from yuyin202109.
* Miaoqi suggested that the files may be broken.
* Developed small program for reading the map file from H432_OH_100_025C_att05_001_0001-1000.hdf into qmap. 
* Met with Miaoqi on how to read or save the mask file after applying ROI using GUI. Additional things I need to do is programming the save button which would ideally save the mask into the qmap file. 
* Looked into how to edit .h5 files: 
    1) [Editing the HDF file](https://quantum-kite.com/category/capabilities/editing-the-hdf-file/)
    2) [How to use HDF5 files in Python](https://www.pythonforthelab.com/blog/how-to-use-hdf5-files-in-python/)

<br />

### September 30, 2021 (Day 23)
Updates:
* Met with Nicholas Schwarz to talk about grad school and career advice. 
* Performed several tests on how to save the mask. Initially, I was unsure how to read the mask and then perform a separate function for saving. However, my function uses Apply ROI to create a new mask and reads it. THe mask is read. For saving, press 'Save' on the GUI. I wired the command to start a function that saves the mask previously read. 
* Saving the new mask onto the existing qmap was tricky. The save function searches the directory for an existing .h5 file, which it assumes to be the one we recently written on based on steps from weeks before. Encountered several errors with writing, but a change in 'w' to 'r+' as command resolved them. The function overwrites existing mask file in the qmap and replaces it wih the new mask. 

<br />

### October 1, 2021 (Day 24)
Updates:
* Presented updates in meeting. Showcased progress to Suresh who was not present last meeting.
* Suresh mentioned needing to establish conditions in the GUI which prevents reading of wrong files. Specifically, this function would be able to differentiate between the raw data files and the meta data files. For instance, the files ending in .h5 or .hd5 will be identified as either raw data or result file to prevent errors in later steps. 
* A potential project has risen from Francesco regarding developing slackbot tools.
* Was having issues regarding reading the new 'yuyin' .h5 files QZ sent. Error message appears saying 'Failed to read scalar dataset. Can't open directory or file.'
* Miaoqi sent link for plugin to hopefully fix this issue. [HDF5 - External filter plugin, installation on Windows 10](https://confluence.desy.de/display/FSEC/HDF5+-+External+filter+plugin%2C+installation+on+Windows+10).

<br />


## Week 6: Improving General GUI Functions/Conditions, Testing QMap

<br />


### October 4, 2021 (Day 25)
Updates:
* Was able to successfully download the plugin environment and open the .h5 files. 
* Incorporated the hdf2sax.py program from last week into the GUI. Was able to generate 2dsaxs and a qmap file from it.
* Examples of plots can be found [here](https://drive.google.com/drive/folders/1Tcb3dGqQR3tp7v4XCuAyJuOjHvlNAct5?usp=sharing).
* Began working on improving conditions/logic for the GUI. For instance, if I were to press the 'save' button, the GUI will resave the mask and not create a new one (or crash). Other examples to work on include the ones mentioned last Friday.
* Rewrote how data was written into the qmap file. Previously, data was all written at once in the beginning after loading of the hdf meta data file. But I decided that data should be written whenever the user decides to (i.e. whenever the buttons are pressed). I think by doing this, I found some errors in how I previously extracted data from the GUI. Hopefully, this improves the new qmaps. I sent one to QZ (for .imm) to analyze. 

<br />

### October 5, 2021 (Day 26)
Updates:
* Attended Student Connects meeting. 
* Met with QZ and Miaoqi to discuss updates to the program.
* QZ ran the new qmap file, said it was good, although with slight discrepancies in one of the plots. We now need to consider implementing a blemish to remove the hot marks (vertical and horizontal lines). 
* Continued working on conditions and other logic. Added conditions which prevent initial loading and reading of incorrect and incorrectly formatted files

<br />

### October 6, 2021 (Day 28)
Updates:
* Had to tend to family emergency.


<br />

### October 7, 2021 (Day 28)
Updates:
* Completed UI updates. This will allow users to receive warning messages if wrong files are used (and cause the program to end).
    1) Added conditions which prevent initial loading and reading of incorrect and incorrectly formatted files
    2) Program will end if directory does not contain desired .bin/.imm/.hdf/.h5 file.
    3) Improved logic behind ‘save’ and ‘compute’ buttons.
* Created PowerPoint to present in tomorrow's meeting. PowerPoint can be found [here](https://drive.google.com/drive/folders/1njXGWVV-lXZ1hiEjk0bqe9wuvRruv3Pm?usp=sharing).


<br />

### October 8, 2021 (Day 29)
Updates:
* Discussed updates and shared results in meeting. 
* Switched focus to blemish files. Was sent .h5 file of blemish. The goal for the blemish is to have it preloaded when using the GUI. Thus, whatever maps that will be created would also have the blemish as well. 
* Will have to generate a qmap fie with the updated dynamic map. 


<br />


## Week 7: Preloading Mask and Blemish Files

<br />


### October 11, 2021 (Day 30)
Updates:
* Played around with operators for the blemish files. Sent some sample results of different operations to QZ and Miaoqi, since I was unsure what the resulting visual representations should look like. QZ confirmed the operation should be logical_and. Examples of the plots can be found [here](https://drive.google.com/drive/folders/1T63eLj3ZlsLOw_NGjli1JDsBMsfkEaLI?usp=sharing).
* Sent QZ the updated qmap, waiting for him to load and test it.

<br />


### October 12, 2021 (Day 31)
Updates:
* Attended Student Connects meeting. 
* Met with QZ and Miaoqi to discuss updates to the program.
* QZ tested the qmap, but two issues need to be addressed. 
    1) Both static and dynamic map should be updated. Not just dynamic map.
    2) The logical_and outputs a file of 1s and 0s while the maps should be 0-36 and 0-360 for dynamic and static, respectively.


<br />

### October 13, 2021 (Day 32)
Updates:
* Made the appropriate changes to the qmap. The plot that is displayed after applying ROI is a multiplication of the static map and dynamic map with the blemish applied. 
* Some issues still come about regarding dimensions. 
* QZ generated a qmap using a triangular mask. While it is  impractical for user support, the goal is to do a rigid comparison between the qmap from Matlab and qmap from Python. He sent me the triangular mask so I can try to replicate the qmap result he attained from Matlab. 
* Worked on triangular mask. Since it was a h5 file, I figured I can upload it the same way as the blemish by preloading it. 
* The triangular mask 'mask_lambda_test.h5' can be found [here](git xxx). 
* A file called 'jeffrey_GUI_test.h5' was also sent, which is the Matlab 'gold standard' qmap result. I can compare the qmap result with this file to see if there are any discrepancies. The difference between both would be a zero matrix. The file can be found [here](git xxx)

<br />

### October 14, 2021 (Day 33)
Updates:
* Errors appear when running as the resulting plots were different. The blemish was inconsistent in the matlab example and in the qmap I created. 
* Discussed with Miaoqi on what could be the issue. It turns out that I should not have replaced the blemish with the triangular mask, thinking they were both served similar purposes. However, I should preload both the blemish and the triangular mask, separately. 
* Worked on making these changes and developing these plots separately from the GUI.

<br />

### October 15, 2021 (Day 34)
Updates:
* Discussed updates and shared results in meeting. 
* Showed the changes I made and the resulting plots achieved. Plotted the differences between the example matlab plot and the one I generated. 
* One thing that should be changed is the restricting/negating the add_roi (mask) function since I am predetermining the mask (triangle). Ideally, we would generate a separate function for drawing a mask and for preloading a mask.
* Will need to configure the GUI to accept these changes. Need to generate a new qmap file.

<br />


## Week 8: Bugs with Dynamic Map and Static Map

<br />


### October 18, 2021 (Day 35)
Updates:
* Made PowerPoint presentation regarding Midpoint Updates for tomorrow's Student Connects meeting. PowerPoint can be found [here](xxx).
* Temporarily inhibited the add_roi function, only allowing preloading blemishes and masks to be implemented. By multiplying the mask with the blemish, you can get the overall mask, which is ultimately applied (mulitplied) by the existing dynamic map or static map. Results can be found [here](xxx).
* I sent the qmap to QZ, apparently the dynamic map does not have any elements of the value 1. Usually, 1 can be found near the center of the dynamic map.


<br />

### October 19, 2021 (Day 36)
Updates:
* Attended Student Connects meeting.
* Ran some tests to find out what could be causing the issue with the lack of 1s. Found other bugs in the program, such as some directories not being updated in the qmap result file. 
* Differences between 'jeffrey_GUI_test.h5' and the dynamic/static maps can be found [here](xxx). 
* Apparently, when preloading the mask to the dynamic map, the mask appears to be placed over the dynamic map. Like an overlap.
* Had meeting with Miaoqi and QZ to discuss my findings. 


<br />

### October 20, 2021 (Day 37)
Updates:
* Worked on trying to resolve issues with the static and dynamic maps.

<br />

### October 21, 2021 (Day 38)
Updates:
* Worked on trying to resolve issues with the static and dynamic maps.
* Created a PowerPoint slide discussing my internship progress updates for Suresh to present in his meeting. Slide can be found [here]().
* Attended safety meeting.

<br />

### October 22, 2021 (Day 39)
Updates:
* Discussed updates and shared results in meeting. 
* Asked Miaoqi to help debug the issue with the static and dynamic maps.


<br />


## Week 9: New GUI Layout, Preloading Mask and Reading Text Function

<br />


### October 25, 2021 (Day 40)
Update:
* Miaoqi was able to fix the issues with the dynamic map and the static map. He also cleaned up the code and resdesigned the UI. 
* Screenshots of the UI can be found [here](xxx). His results (and comparisons with 'jeffrey_GUI_test.h5') can be found [here](xxx).
* Learned how to use the new functions present in the GUI. 
* Miaoqi's GUI has a temporary function for preloading masks in the backend, but nothing is wired on the GUI. I plan to work on the preloading function as well as adding additional functions to the GUI where I see fit. 

<br />

### October 26, 2021 (Day 41)
Update:
* Attended Student Connects meeting. 
* Met with QZ and Miaoqi to discuss updates to the program.
* Attended APS Division meeting.
* Created buttons/added logic for preloading masks. 
    1) GUI is capable of importing files for masks, with the option of providing the location of the directory in the HDF file. 
    2) Select button reads the mask file after importing.
    3) Preview button presents the mask on the interface. Still having issues with this, since my function removes other plots.
    4) Apply Mask multiplies the mask with the dynamic map. 


<br />

### October 27, 2021 (Day 42)
Update:
* Tried to fix issues with plotting preview mask. 
* Added a new section in the dropdown bar and a new plot index dedicated for preview. Still not successful.
* Worked on function for reading blemishes/hot pixels found by users. The original Matlab file can be found [here](git xxx) as a text file. Specifically, we will be looking at Lambda750K. 
* Manually took all the matlab coordinates and put them into the text file. Created another import file bar specifically for these text files. 
* The new function reads the text file and separates the coordinates into x and y values, subtracts one to adjust from matlab to python. 

<br />

### October 28, 2021 (Day 43)
Update:
* Made some finalizing touches to the blemish text file function. It can be found [here](git xxx).
* Started working on a separate program for calculating direct beam. The original program was developed by QZ in matlab and can be fond [here](git xxx).
* Looked into a lot of Matlab syntax and functions. Resources:
    1) [x](xxx)
* Had a lot of questions when converting the code, need to ask for help from Miaoqi or QZ. 

<br />

### October 29, 2021 (Day 44)
Update:
* Presented updates at group meeting. QZ was absent in this meeting.
* Suresh suggested working and talking with Henry to discuss potentials in combining our two projects. Miaoqi had other ideas that he wanted to implement to the GUI. 
* Created a branch on the APS/pysimple mask of my updates to the GUI.
* Discussed in greater details to Miaoqi on the changes I made. He answered some of my questions regarding the Matlab conversion. 



<br />




## Week 10: Further Additions to GUI

<br />


### November 1, 2021 (Day 45)
Updates:
* Had to tend to family emergency.
<br />

### November 2, 2021 (Day 46)
Updates:
* Attended meeting with Pete Jemian and QZ for possible work to be done on Bluesky. Bluesky is a Python platform used at APS for XPCS. 
* Attended Student Connects meeting. 
* Met with QZ and Miaoqi to discuss updates to the program.
* Made some additions for reading command line arguments for the direct beam calculation code. Need to ask QZ in groupchat for help.

<br />

### November 3, 2021 (Day 47)
Updates:
* Updated Git Repo in terms of pushing new changes and cleaning up directories. 
* Caught up on logs and uploading files/links. 
* Previewed and played around with Henry's GUI program for wide-angle. 


<br />

### November 4, 2021 (Day 48)
Updates:
* 


<br />

### November 5, 2021 (Day 49)

<br />



<!-- ## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6 -->
