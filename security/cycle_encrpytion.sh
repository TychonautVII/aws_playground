aws-encryption-cli --encrypt \
                --master-keys key=arn:aws:kms:us-east-1:455819476927:key/07e8f93b-b878-4e91-b58a-4b6c04f0a7b6 profile=personal1 \
                --input alice_in_wonderland.7z \
                --metadata-output alice_in_wonderland_encrypt.meta \
                --output alice_in_wonderland.7z.encrypted 

aws-encryption-cli --decrypt \
                     --input alice_in_wonderland.7z.encrypted  \
                    --master-keys profile=personal1 \
                     --metadata-output alice_in_wonderland_decrypt.meta \
                     --output alice_in_wonderland_decrypted.7z 
