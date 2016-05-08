
run key bits tester
--------------------------------------------------------------------------------
message source: 
"Python was conceived in the late 1980s,[30] and its implementation began in December 1989[31] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL)[32] capable of exception handling and interfacing with the operating system Amoeba.[7] Van Rossum is Python's principal author, and his continuing central role in deciding the direction of Python is reflected in the title given to him by the Python community, benevolent dictator for life (BDFL).About the origin of Python, Van Rossum wrote in 1996:[33]"
--------------------------------------------------------------------------------
key mask:  3
--------------------------------------------------------------------------------
keys: 
[(8, '53'),
 (16, '53d4'),
 (32, '53d42ffe'),
 (64, '53d42ffefe5c71be'),
 (128, '53d42ffefe5c71befa625b1e093463db'),
 (256, '53d42ffefe5c71befa625b1e093463db65e4c77e1a67c0b4aeab205d7b17bd69')]
--------------------------------------------------------------------------------
Tester Result: 
            key         status     runtime(s)

              8        success       0.014081
             16        success       0.022192
             32        success       0.039784
             64        success       0.074691
            128        success       0.143053
            256        success       0.278241
--------------------------------------------------------------------------------
Time Consuming Growing: 

                                 key bits growing

       +---------+---------+----------+---------+---------+---------+------+
  0.35 +-+       +         +          +         +         +         +    +-+
       |'-' ***E***                                                        |
   0.3 +-+                                                               +-+
       |                                                 **E               |
  0.25 +-+                                           ****                +-+
       |                                         ****                      |
       |                                    *****                          |
   0.2 +-+                              ****                             +-+
       |                            ****                                   |
  0.15 +-+                     **E**                                     +-+
       |                   ****                                            |
   0.1 +-+             ****                                              +-+
       |           *E**                                                    |
       |        ***                                                        |
  0.05 +-+  **E*                                                         +-+
       + EE*     +         +          +         +         +         +      |
     0 +-+-------+---------+----------+---------+---------+---------+----+-+
       0         50       100        150       200       250       300
                                     key/bits

--------------------------------------------------------------------------------
run message length tester
--------------------------------------------------------------------------------
encrypt key:  53d42ffefe5c71be
--------------------------------------------------------------------------------
mask:  5
--------------------------------------------------------------------------------
test turns:  13
--------------------------------------------------------------------------------
Tester Result: 
    message len         status     runtime(s)

     32.0 bytes        success       0.005337
     64.0 bytes        success       0.009245
    128.0 bytes        success       0.017213
    256.0 bytes        success       0.033141
    512.0 bytes        success       0.065595
         1.0 kB        success       0.129233
         2.0 kB        success       0.259227
         4.0 kB        success       0.509977
         8.0 kB        success       1.014864
        16.0 kB        success       2.037301
        32.0 kB        success       4.115034
        64.0 kB        success       8.375579
       128.0 kB        success      17.140181
--------------------------------------------------------------------------------
Time Consuming Growing: 

                                 message growing

     +-------+-------+--------+-------+-------+-------+--------+-------+---+
     +       +       +        +       +       +       +        +       +   |
  20 +'-' ***E***                                                        +-+
     |                                                                     |
     |                                                    *E               |
     |                                                ****                 |
  15 +-+                                          ****                   +-+
     |                                        ****                         |
     |                                    ****                             |
  10 +-+                              ****                               +-+
     |                            ****                                     |
     |                        **E*                                         |
     |                   *****                                             |
   5 +-+             ****                                                +-+
     |         ***E**                                                      |
     |    **E**                                                            |
     +  E*   +       +        +       +       +       +        +       +   |
   0 EEE-----+-------+--------+-------+-------+-------+--------+-------+-+-+
     0     20000   40000    60000   80000   100000  120000   140000  160000
                                  message/bytes

--------------------------------------------------------------------------------
