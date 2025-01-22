#!/bin/bash
source ../remote_config/.env

sshpass -p "$REMOTE_PASSWORD" ssh "${REMOTE_USER}@${REMOTE_HOST}" "bash ${REMOTE_GET_DATA_SCRIPT}"
sshpass -p "$REMOTE_PASSWORD" scp "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_FILE_PATH}" "${LOCAL_FILE_PATH}"