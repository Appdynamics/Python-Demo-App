#!/bin/bash

if [ -z "${CONTROLLER}" ]; then
        export CONTROLLER="controller";
fi

if [ -z "${APPD_PORT}" ]; then
        export APPD_PORT=8090;
fi

if [ -z "${SSL}" ]; then
        export SSL="ssl should be off";
fi

if [ -z "${ACCOUNT_NAME}" ]; then
        export ACCOUNT_NAME="analytics-customer1";
fi

if [ -z "${ACCESS_KEY}" ]; then
        export ACCESS_KEY="your-account-access-key";
fi

if [ -z "${BUNDY_TIER}" ]; then
        export BUNDY_TIER="Bundy";
fi
