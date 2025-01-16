# ABA Session Note Generator

## Approach and challenge

- Create required endpoints to support frontend functionality.
- Connect server with OpenAI endpoint to generate notes

*Note*: Create a variable called `OPENAI_KEY` in an `.env` file before running the server.

#### Endpoints specification:

- Generate notes using AI:

```
    request
        input: str
        duration: seconds
        type: str

    response:
        generated_note: str
```
		
- Save generated notes:

```
	request:
		input: str
		therapist_id: str
    response:
        success: bool
        error: str
```
		
- Load saved notes:

```
	request:
        therapist_id: str
		start_date: datetime
		end_date: datetime
	response:
		notes: List[Note]
		
	Note (creation_time, content, therapist_id)
```

## Design decisions

- Use [pydantic] to model endpoint request and responses
- Add a basic validation and error control. TODO: Add more validations and tests
- Keep secrets in `.env` file. TODO: Use a secrets manager.


#### Typing support

We use `orval` to synchronize types from Backend into the frontend. It improves consistency and reduce future work.

## Assumptions

- Data is not persistent (no DB attached)
- Code structure can be improved (i.E. Using different files and modules).
- ASsumes only one therapist, Missing implementation of therapist_id filters.

## Sources

- [Orval docs](https://orval.dev/)