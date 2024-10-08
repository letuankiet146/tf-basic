import tensorflow as tf

PRICE_OF_PRODUCT = tf.constant([[1, 2, 3]])
print(PRICE_OF_PRODUCT)
HISTORY_SALE = tf.constant([
    #M #T  #W #THu
    [4, 8 ,9, 12],
    [5, 1, 8, 10],
    [12, 7, 3, 8],
])
print (HISTORY_SALE)
print ("Revenue of four days")
print (tf.matmul(PRICE_OF_PRODUCT, HISTORY_SALE))