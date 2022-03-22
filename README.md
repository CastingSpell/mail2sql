Simple email parser that keeps listening on a mailbox, detecting when a new email is received and parsing the data. Then makes an insert in an external database, updating the current values to be displayed on third-party apps


***
Received email template
~~~
Subject: *****************************************************************************************************
Date: *******************
From: **********************************
To: **********************************

********** local 12345 ***************************************************
************************

****************
**********************************************
*********************************
*********
****************

*****************************
*************************

*****************

     * CIST-00-T1-00 a T0 (123ABC) => 100.0 L.
     * CIST-00-T1-00 a T1 (123ABC) => 100.0 L.

***********************************************************************
~~~
