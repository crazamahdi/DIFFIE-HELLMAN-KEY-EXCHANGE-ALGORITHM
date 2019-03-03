# DIFFIE-HELLMAN-KEY-EXCHANGE-ALGORITHM
Diffie Hellman key exchange establishes a shared secret between two parties that can be used for secret communication for exchanging data over a public network and actually uses public key techniques to allow the exchange of a private encryption key.

Algorithm
Step 1 : Select q which should be a Prime Number.

Step 2 : Select α a Primitive Root of q.

Step 3 : User A Key Generation -

     a.	Select a positive Number XA < q.
     
     b.	Calculate Public Exponent of A , YA = α^XA mod q.
Step 4 : User B Key Generation -

     a.	Select a positive Number XB < q.
     
     b.	Calculate Public Exponent of A , YB = α^XB mod q.
Generate Secret Key of User A i.e KA = YB^XA mod q.

Generate Secret Key of User B i.e KB = YA^XB mod q.
