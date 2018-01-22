# build_stats
Build Logs Statistics and Analysis Server

## Installation

```
pip install --user -r requirements.txt
```

## API

Internal:

  |                 |                                         |
  |-----------------|-----------------------------------------|
  | **Title**       | Control Build Timer                     |
  | **URL**         | **/build**                              |
  | **Method**      | **POST**                                |
  | **URL Params**  | None                                    |

**Data Params**:
```
{
   "build": {
        "device": [string],
        "action": "start"|"stop"
    }
}
```

External:

|                |                             |
|----------------|-----------------------------|
| **Title**      | Get Device Stats            |
| **URL**        | **/stats**                  |
| **Method**     | **GET**                     |
| **URL Params** | Required: `device=[string]` |

## Usage Example

To launch the server:

```
gunicorn stats:api
```

To request a device status:

```
curl -X GET "<ip>:<port>/stats?device=mako"
```
