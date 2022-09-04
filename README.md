# Love-sms
Love sms is a lambda that runs periodically 1 time per day, which sends a random sms to your platonic love  💑.

## Steps

1. Run `pip install chalice`
2. Create VirtualEnv with requeriments.txt
3. Set `AMAZON_ACCESS_KEY_ID`, `AMAZON_SECRET_ACCESS_KEY` and `AMAZON_SNS_REGION_NAME` with your amazon credentials in `config.json` file
4. Set `RECEIVER_PHONE` in `config.json` file, this is the phone number of your crush 😹😻, example: `57301588xxxx`
5. For deploy in local run `chalice local`
6. For deploy in AWS run `chalice deploy`
