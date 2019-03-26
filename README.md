
# Define sample data

In order to load your sample (generated from botvac application), you need to modify the following parts: 


Find this line and insert your code bellow that:
````
### Insert your definition here
````
The code like:
````
if name == 'sample_name':
    for i in range(start_number, end_number):
        filename = 'direction_to_folder' + str(i) + '.pkl'
        scan = read_file(filename)
        self._scans.append(scan)
````
you also need to modify that:
````
DATA = 'sample_name'
````
# Run the program
Run the run.bat file, wait for a while and access to http://127.0.0.1:5000. When a browser loading the page, it will load and visualize through each sample simultaneously, you can pause it by pressing the button.

![Screenshot](image1.png "Logo Title Text 1")        

# Check angle information

Basically, you can see the information about a angle by providing the angle number into the field and pressing the look up button.

Moreover, you can just move the mouse cursor to a dot that you want to lookup, recommend that pause the loading process.
 
# Comparing two samples
compare 2 samples separately by 2 colors to see the difference by accesing to URI 
````
http://127.0.0.1:5000/compare
````
Modify that line:
````
DATA = "sample_1"
DATA_TO_COMPARE = "sample_2"  # Optional
````
Note: you need to define for the 'sample_2', see Define sample data part for more detail.
