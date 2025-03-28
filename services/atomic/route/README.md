# Locating Service

A route optimiser service that plans the most time efficient route to pickup food items from reserved hubs.

## Overview

This service uses the Directions API in Google Maps API to come up with an optimal, step-by-step route for the food bank's pickup driver's reference.

## API


### getFilteredUsers

Filters a list of volunteer users based on their proximity to a center point between a product 
location and the nearest community center.

**Request**:
- `foodbankID`: Unique identifier for the food bank
- `foodbankName`: Name of the food bank
- `foodbankAddress`: Address of the food bank
- `reservedHubs`: List of {hubID, hubName, hubAddress} that requires collection from food bank

**Response**:
- `foodbankName`: Name of the food bank
- `foodbankAddress`: Address of the food bank
- `route`: Optimized route containing a sorted list of {hubName, hubAddress}, so driver from food bank can input into his own Google Maps app from the UI

- `error`: Error message if any occurred

## Environment Variables

## Building and Running
build and run docker compose

# Install dependencies
pip install -r requirements.txt

# Run the service
python route.py