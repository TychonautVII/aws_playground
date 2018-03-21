# You have to be in a directory with the json files, and you have to have a profile with a region set

aws iam create-service-linked-role --aws-service-name lex.amazonaws.com --profile peter-personal

aws lex-models put-slot-type \
    --name FlowerTypes \
    --cli-input-json file://FlowerTypes.json --profile peter-personal

aws lex-models put-intent \
   --name OrderFlowers \
   --cli-input-json file://OrderFlowers.json --profile peter-personal

aws lex-models put-bot \
    --name OrderFlowersBot \
    --cli-input-json file://OrderFlowersBot.json --profile peter-personal

 aws lex-models get-bot \
    --name OrderFlowersBot \
    --version-or-alias "\$LATEST" --profile peter-personal

 aws lex-runtime post-text \
    --bot-name OrderFlowersBot \
    --bot-alias "\$LATEST" \
    --user-id UserOne \
    --input-text "i would like to order flowers" \
    --profile peter-personal