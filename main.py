from hashlib import sha256
MAX_NONCE=10000000
def SHA256(text):
    return (sha256(text.encode("ascii")).hexdigest())

def mine(block_number,transaction,prev_hash,prefix_zeroes):
    for nonce in range(MAX_NONCE):
        prefix_str = '0'*prefix_zeroes
       # nonce=1
        text=str(block_number)+transaction+prev_hash+str(nonce)
        new_hash=SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Successfull Mining of Bitcoin nonce:{nonce}")
            return new_hash
    raise BaseException(f"Couldn't find correct after :{MAX_NONCE} times")

if __name__=='__main__':
    transaction='''
    Shouhardik->Siya->34
    Sara->Varun->78
    '''
    difficulty=5
    import time
    start=time.time()
    print("start mining")
    new_hash=mine(5,transaction,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7',difficulty)
    total_time=str(time.time()-start)
    print(f"Completed in :{total_time} seconds")
    print(new_hash)
