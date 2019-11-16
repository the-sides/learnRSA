python3.7 ./rsa-keygen -p key.pub -s key -n 4096 
echo '\n++++++++++++++++++++++++++++++++'
echo 'public key (key.pub) contents'
echo '++++++++++++++++++++++++++++++++'
cat key.pub
echo '\n++++++++++++++++++++++++++++++++'
echo 'private key (key) contents'
echo '++++++++++++++++++++++++++++++++'
cat key
echo '\n++++++++++++++++++++++++++++++++'
echo 'Encrypting message...'
echo '++++++++++++++++++++++++++++++++'
cat msg
python3.7 rsa-enc -k key.pub -i msg -o output
echo '\n++++++++++++++++++++++++++++++++'
echo 'Decrypted message (washed)...'
echo '++++++++++++++++++++++++++++++++'
python3.7 rsa-dec -k key -i output -o washed 
echo '================ message =============='
cat washed
# rm -rf key.pub key
echo 'deleting key...'
