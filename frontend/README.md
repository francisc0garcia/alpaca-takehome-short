# ABA Session Note Generator

## Approach and challenge

- Generate types from the backend using Orval
- Integrate API methods in to the corresponding page/component
- Provide feedback to user when calling endpoints

## Design decisions

- Mock methods for API calls are available, but not yet implemented.
- By default, we use axios as http client, but can also configure fetch is required.
- Keep user feedback simple: use standard alerts. (due to time constrains).
- Use `moment.js` to offer therapist a more convenient way of reading Session date time.

## Assumptions

- Type names are generated using defaults. They can be improved later. (i.E. `generateNoteGenerateNotePost` -> `generateNotePost`)

## Sources

- [Orval docs](https://orval.dev/)
