hdpr01mgt:

/etc/oozie/conf/log4j.properties

```
log4j.appender.oozie.RollingPolicy.MaxHistory=168
log4j.appender.oozieError.RollingPolicy.MaxHistory=168
```

find /var/log/oozie -type f -mtime +7 -delete

