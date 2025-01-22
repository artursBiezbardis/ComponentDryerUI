#!/bin/bash
source ../remoute_config/.env

sshpass -p "$REMOTE_PASSWORD" ssh "${REMOTE_USER}@${REMOTE_HOST}" "bash ${REMOTE_UPDATE_TIME_SCRIPT}"

