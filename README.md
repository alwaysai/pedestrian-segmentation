# Pedestrian Segmentation
This app expands on the *semantic_segmentation_cityscape* starter app to build an app that segments pedestrians and bicyclists in each frame of a video, and performs actions based on the results. The full tutorial can be found on the [alwaysAI blog](https://learn.alwaysai.co/how-to-detect-pedestrians-and-bicyclists-in-a-cityscape-video).

## Setup
This app requires an alwaysAI account. Head to the [Sign up page](https://www.alwaysai.co/dashboard) if you don't have an account yet. Follow the instructions to install the alwaysAI toolchain on your development machine.

Next, create an empty project to be used with this app. When you clone this repo, you can run `aai app configure` within the repo directory and your new project will appear in the list.

You'll need to supply your own input video and update the file path in `FileVideoStream`.

## Usage
Once the alwaysAI toolset is installed on your development machine (or edge device if developing directly on it) you can run the following CLI commands:

To set up the target device & folder path

`aai app configure`

To build and deploy the docker image of the app to the target device

`aai app deploy`

To start the app

`aai app start`

