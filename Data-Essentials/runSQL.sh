#!/bin/bash
# Runs the SQL provided
sqlite3 << EOF
.read $1
.exit
EOF
