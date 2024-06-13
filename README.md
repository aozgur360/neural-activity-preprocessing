"# neural-activity-preprocessing" 

pipeline_main:
The main pipeline used was fully developed by the creators of Minian: https://github.com/denisecailab/minian.
Code is shared here for the exact parameters I used, with some adjustments for batching across all subjects.
This is used to find all neurons active in the recorded session from the miniscope videos.
It also will determine the level of calcium fluorescence activity at each frame.
![fig32_cellmatching_images_raw](https://github.com/aozgur360/neural-activity-preprocessing/assets/77759136/9d64ef6c-06be-4d33-876f-142b15254525)


cross-registration1:
Also developed by the creators of Minian to track cells across sessions. I modified this with my desired parameters and added
batch processing in the following script - cross-registration1_auto.
*![fig33_cellmatching_images_processsed](https://github.com/aozgur360/neural-activity-preprocessing/assets/77759136/3e320927-3feb-4eee-a20f-3b8a54f84ec7)


bloodvessels:
This script is used to exclude cells based on a size or shape threshold. This is important since sometimes the original pipeline
may misidentify bloodvessels as neurons (see yellow arrows in image above for excluded entities).

python_analysis_detect_plus_minian_automate_hbug_detection:
Used to determine what sessions need to be ran. This will provide a list of sessions that can be copied into pipeline_main for batch processing.
It also will determine which sessions need to be run for miniscope video quality checks.
These sessions should be ran using the following MatLab code developed by Branden Clark (Branden99clark@gmail.com), hbug_052622_txt_file_batch.mlx
have an error in any frames of the recorded miniscope video where the are horizontal noise lines in the image, as seen below (I commonly refer to this bug as 'hbug').

![hbug_ex](https://github.com/aozgur360/neural-activity-preprocessing/assets/77759136/48b7466b-03e4-47a9-a686-e49c7eeb934d)

![Capture](https://github.com/aozgur360/neural-activity-preprocessing/assets/77759136/68b3c9cd-0273-4cdf-85ce-e6e47b45b31f)

get_spikerate:
Used to get spikerate file when desired, instead of the output of only the raw calcium traces.

graph_spikerate_and_rawcalcium:
Used to visualize the differences in calcium traces between raw calcium and spikerate.
*insert image*

