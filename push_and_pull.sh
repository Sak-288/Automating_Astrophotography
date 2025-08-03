#!/bin/bash
git add .
git commit -m "$1"
git push origin main && ssh sakam@raspberrypi.local '~/auto_pull.sh'

