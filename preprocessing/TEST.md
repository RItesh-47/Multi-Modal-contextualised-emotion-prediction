```ps1
(curl http://localhost:8080/api/annotations/1 -H @{Authorizations="Token 5c64d04c2690d888ed9e4ada77b7132870c693f7"}).Content
```


```json
{
    "main-category": {
        "Emotion": true/false,
        "Humor": true/false,
        "Sarcasm": true/false
    },
    "emotion-type-coarse": ["positive", "negative", "neutral"], // take one from the list
    "emotion-type-fine": {
        "positive": {
            "Admiration": 0-10,
            "Love": 0-10,
            "Optimism": 0-10,
            "Joy": 0-10,
            "Excitement": 0-10,
            "Caring": 0-10,
            "Approval": 0-10,
            "Desire": 0-10,
            "Relief": 0-10,
            "Amusement": 0-10,
            "Pride": 0-10
        }, OR
        "negative": {
            "Annoyance": 0-10,
            "Disapproval": 0-10,
            "Anger": 0-10,
            "Disgusting": 0-10,
            "Sadness": 0-10,
            "Nervousness": 0-10,
            "Fear": 0-10,
            "Embarrassment": 0-10,
            "Remorse": 0-10,
            "Disappointment": 0-10,
            "Grief": 0-10
        }, OR
        "neutral":{
            "Realisation": 0-10,
            "Curiosity": 0-10,
            "Confusion": 0-10,
            "Surprise": 0-10,
        }
    }
}

```