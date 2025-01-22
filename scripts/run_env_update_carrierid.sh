#!/bin/bash
source ../remoute_config/.env

sshpass -p "$REMOTE_PASSWORD" ssh "${REMOTE_USER}@${REMOTE_HOST}" "cat > ${REMOTE_ENV_FILE_PATH}" < ${LOCAL_ENV_FILE_PATH}

