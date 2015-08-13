#! /bin/bash

. /etc/profile

app_path="/home/deployer/smzdm_checkin_daily"

cd $app_path

case "$1" in
  start)
      /usr/bin/python $app_path/smzdm.py start &
     ;;
  *)
        echo $"Usage: $0 {start}"
        exit 1
esac

exit 1
