# You have to be in a directory with the json files, and you have to have a profile with a region set

aws iam create-service-linked-role --aws-service-name lex.amazonaws.com --profile peter-personal

aws lex-models put-slot-type \
    --region us-east-1 \
    --name FlowerTypes \
    --cli-input-json file://FlowerTypes.json --profile peter-personal

aws lex-models put-intent \
   --region us-east-1 \
   --name OrderFlowers \
   --cli-input-json file://OrderFlowers.json --profile peter-personal

aws lex-models put-bot \
    --region us-east-1 \
    --name OrderFlowersBot \
    --cli-input-json file://OrderFlowersBot.json --profile peter-personal

 aws lex-models get-bot \
    --region us-east-1 \
    --name OrderFlowersBot \
    --version-or-alias "\$LATEST" --profile peter-personal

 aws lex-runtime post-text \
    --region us-east-1 \
    --bot-name OrderFlowersBot \
    --bot-alias "\$LATEST" \
    --user-id UserOne \
    --input-text "i would like to order flowers" \
    --profile peter-personal