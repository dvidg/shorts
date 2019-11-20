#!/bin/bash

curl -X POST \
  https://api.strava.com/api/v3/push_subscriptions \
  -F client_id=40821 \
  -F client_secret=f44c98714f2115cb6951f129d45a184037676139 \
  -F callback_url=https://5fe74b16.ngrok.io/webhook \
  -F verify_token=STRAVA
