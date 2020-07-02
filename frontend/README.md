# Frontend React Native application for ACNH Item OCR

The following steps apply to Android development on a Windows machine.

## Setup

To run the frontend, you will need Node, the React Native command line interface, Python2, a JDK, and Android Studio.

Instructions for installing these dependencies can be found [here](https://reactnative.dev/docs/environment-setup) under **React Native CLI Quickstart**.

## Installing Dependencies

From the `\frontend` folder, install the packages by running:

```
cd acnh-item-ocr\frontend
npm install
```

## Running the Application

First, we'll need to start the [Metro Bundler](facebook.github.io/metro/)

```
npm run start
```

Next, we'll start the Android application:

```
npm run android
```
