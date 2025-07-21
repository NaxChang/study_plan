#!/bin/bash 

echo "Hi ${username:-default}"

username=user

echo "Hi ${username:-default}"