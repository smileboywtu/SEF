
                                   time growing

       +---------+---------+----------+---------+---------+---------+------+
  0.35 +-+       +         +          +         +         +         +    +-+
       |                                                       '-' ***A*** |
   0.3 +-+                                                               +-+
       |                                                 **A               |
  0.25 +-+                                           ****                +-+
       |                                         ****                      |
       |                                    *****                          |
   0.2 +-+                              ****                             +-+
       |                            ****                                   |
  0.15 +-+                     **A**                                     +-+
       |                   ****                                            |
   0.1 +-+             ****                                              +-+
       |           *A**                                                    |
       |        ***                                                        |
  0.05 +-+  **A*                                                         +-+
       + AA*     +         +          +         +         +         +      |
     0 +-+-------+---------+----------+---------+---------+---------+----+-+
       0         50       100        150       200       250       300
                                     key/bits


                                  time growing

     +-------+-------+--------+-------+-------+-------+--------+-------+---+
  20 +-+     +       +        +       +       +       +        +       + +-+
     |                                                         '-' ***A*** |
     |                                                                     |
     |                                                   **A               |
  15 +-+                                             ****                +-+
     |                                          *****                      |
     |                                      ****                           |
     |                                 *****                               |
  10 +-+                           ****                                  +-+
     |                         *A**                                        |
     |                     ****                                            |
     |                  ***                                                |
   5 +-+            ****                                                 +-+
     |         ***A*                                                       |
     |    **A**                                                            |
     +  A*   +       +        +       +       +       +        +       +   |
   0 AAA-----+-------+--------+-------+-------+-------+--------+-------+-+-+
     0     20000   40000    60000   80000   100000  120000   140000  160000
                                  message/bytes

[1;34;47mrun key bits tester[0m
--------------------------------------------------------------------------------
[1;36;40mmessage source: [0m
"Python was conceived in the late 1980s,[30] and its implementation began in December 1989[31] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL)[32] capable of exception handling and interfacing with the operating system Amoeba.[7] Van Rossum is Python's principal author, and his continuing central role in deciding the direction of Python is reflected in the title given to him by the Python community, benevolent dictator for life (BDFL).About the origin of Python, Van Rossum wrote in 1996:[33]"
--------------------------------------------------------------------------------
[1;36;40mkey mask: [0m 3
--------------------------------------------------------------------------------
[1;36;40mkeys: [0m
[(8, '53'),
 (16, '53d4'),
 (32, '53d42ffe'),
 (64, '53d42ffefe5c71be'),
 (128, '53d42ffefe5c71befa625b1e093463db'),
 (256, '53d42ffefe5c71befa625b1e093463db65e4c77e1a67c0b4aeab205d7b17bd69')]
--------------------------------------------------------------------------------
[1;36;40mTester Result: [0m
            key         status        runtime

              8        success       0.013785
             16        success        0.02304
             32        success       0.049847
             64        success       0.083116
            128        success       0.154514
            256        success       0.280402
--------------------------------------------------------------------------------
[1;36;40mTime Consuming Growing: [0m
--------------------------------------------------------------------------------
[1;34;47mrun message length tester[0m
--------------------------------------------------------------------------------
[1;36;40mencrypt key: [0m 53d42ffefe5c71be
--------------------------------------------------------------------------------
[1;36;40mmask: [0m 5
--------------------------------------------------------------------------------
[1;36;40mtest turns: [0m 13
--------------------------------------------------------------------------------
[1;36;40mTester Result: [0m
    message len         status        runtime

     32.0 bytes        success        0.00969
     64.0 bytes        success       0.013415
    128.0 bytes        success       0.021599
    256.0 bytes        success       0.034523
    512.0 bytes        success       0.066302
         1.0 kB        success       0.129571
         2.0 kB        success       0.263514
         4.0 kB        success       0.538392
         8.0 kB        success       1.034362
        16.0 kB        success       2.046466
        32.0 kB        success       4.225531
        64.0 kB        success       8.392625
       128.0 kB        success      16.472235
--------------------------------------------------------------------------------
[1;36;40mTime Consuming Growing: [0m
--------------------------------------------------------------------------------
