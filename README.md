# Pedestrian Segmentation
This app expands on the *semantic_segmentation_cityscape* starter app to build an app that segments pedestrians and bicyclists in each frame of a video, and performing actions based on the results. The full tutorial can be found on the [alwaysAI blog](https://learn.alwaysai.co/how-to-detect-pedestrians-and-bicyclists-in-a-cityscape-video).

## Setup
This app requires access to alwaysAI's Beta program. To sign up go to the [Sign up page](https://www.alwaysai.co/dashboard)

Once accepted to the program, follow the setup instructions located on the [Docs page](https://www.alwaysai.co/docs/getting_started/introduction.html) - Note this link is accessible only to beta users.

## Usage
Once the alwaysAI toolset is installed on your development machine (or edge device if developing directly on it) you can run the following CLI commands:

To set up the target device & folder path

`aai app configure`

To build and deploy the docker image of the app to the target device

`aai app deploy`

To start the app

`aai app start`

You'll need to supply your own input video and update the file path in `FileVideoStream`.
