
# Context
[Architect: ## Implementation approach
To implement the airplane speedometer gauge application for iOS devices, we will follow the following approach:

1. **Real-time representation of speed and other metrics**: We will use the Core Location framework to access the device's GPS data and retrieve the speed and other relevant metrics in real-time.

2. **Customization options for visual elements**: We will leverage the power of Core Animation to create customizable visual elements for the speedometer gauge, such as the rim, face, and ticks. We will use open-source libraries like SwiftSVG or SVGKit to import vector graphics for the visual elements.

3. **Smooth visual transitions**: We will utilize Core Animation to create smooth visual transitions and animations for the speedometer gauge. We can use open-source libraries like Lottie or Hero to simplify the animation implementation.

4. **Adjust, save, and retrieve gauge metrics using Core Data**: We will use Core Data to store and manage the gauge metrics. Core Data provides a powerful and efficient way to persist data in iOS applications. We can use open-source libraries like CoreDataKit or MagicalRecord to simplify the Core Data implementation.

5. **Compatibility across iOS devices**: We will ensure compatibility across different iOS devices, including iPad and iPhone, by utilizing the Auto Layout system provided by UIKit. Auto Layout allows us to create adaptive user interfaces that adjust to different screen sizes and orientations.

6. **Intuitive user experience**: We will focus on creating a clean and intuitive user interface that is easy to navigate and understand. We can use open-source libraries like SnapKit or PureLayout to simplify the layout and constraint management.

7. **Synchronization capabilities with other aviation-related iOS applications**: We will implement synchronization capabilities by integrating with aviation-related APIs or by implementing data exchange protocols like JSON or XML. We can use open-source libraries like Alamofire or SwiftyJSON to simplify the networking and data parsing tasks.

## Swift Package Name
```swift
"AirplaneSpeedometerGauge"
```

## File List
```swift
[
    "MainViewController.swift",
    "SpeedometerView.swift",
    "CustomizationViewController.swift",
    "DataStorageManager.swift",
    "NetworkingManager.swift",
    "Models/SpeedometerMetrics.swift",
    "Helpers/AnimationHelper.swift",
    "Helpers/LocationHelper.swift",
    "Helpers/UserDefaultsHelper.swift",
    "Helpers/NetworkHelper.swift",
    "Resources/Assets.xcassets",
    "Resources/CustomizationOptions.json",
    "Resources/NetworkingConfig.plist"
]
```

## Data Structures and Interface Definitions
```mermaid
classDiagram
    class MainViewController{
        -SpeedometerView speedometerView
        -CustomizationViewController customizationViewController
        -DataStorageManager dataStorageManager
        -NetworkingManager networkingManager
        +void viewDidLoad()
        +void updateSpeedometerMetrics(SpeedometerMetrics metrics)
        +void saveSpeedometerMetrics(SpeedometerMetrics metrics)
        +SpeedometerMetrics retrieveSpeedometerMetrics()
        +void syncWithOtherApps()
    }

    class SpeedometerView{
        -UIImageView rimImageView
        -UIImageView faceImageView
        -UIImageView ticksImageView
        -UILabel speedLabel
        +void setSpeed(int speed)
        +void setRimImage(UIImage image)
        +void setFaceImage(UIImage image)
        +void setTicksImage(UIImage image)
    }

    class CustomizationViewController{
        -UITableView customizationOptionsTableView
        -[CustomizationOption] customizationOptions
        +void viewDidLoad()
        +void saveCustomizationOptions()
    }

    class DataStorageManager{
        +void saveMetrics(SpeedometerMetrics metrics)
        +SpeedometerMetrics retrieveMetrics()
    }

    class NetworkingManager{
        +void syncWithOtherApps()
    }

    class SpeedometerMetrics{
        +int speed
        +int yaw
        +int otherMetrics
    }

    class AnimationHelper{
        +void animateSpeedometerView(SpeedometerView speedometerView, SpeedometerMetrics metrics)
    }

    class LocationHelper{
        +void startUpdatingLocation()
        +void stopUpdatingLocation()
        +CLLocationCoordinate2D getCurrentLocation()
        +double getCurrentSpeed()
    }

    class UserDefaultsHelper{
        +void saveObject(object: Any, forKey: String)
        +Any retrieveObject(forKey: String)
    }

    class NetworkHelper{
        +void sendRequest(url: URL, parameters: [String: Any], completion: (Data?, Error?) -> Void)
        +void parseResponse(data: Data) -> [String: Any]
    }
```

## Program Call Flow
```mermaid
sequenceDiagram
    participant M as MainViewController
    participant S as SpeedometerView
    participant C as CustomizationViewController
    participant D as DataStorageManager
    participant N as NetworkingManager
    participant A as AnimationHelper
    participant L as LocationHelper
    participant U as UserDefaultsHelper
    participant H as NetworkHelper

    M->>+S: viewDidLoad()
    M->>+D: viewDidLoad()
    M->>+N: viewDidLoad()
    M->>+L: viewDidLoad()
    M->>+U: viewDidLoad()

    M->>+L: startUpdatingLocation()
    L->>-M: getCurrentSpeed()
    M->>+S: setSpeed(speed)

    M->>+D: retrieveSpeedometerMetrics()
    D->>-M: SpeedometerMetrics
    M->>+S: setRimImage(image)
    M->>+S: setFaceImage(image)
    M->>+S: setTicksImage(image)

    M->>+C: viewDidLoad()
    C->>-M: customizationOptions
    M->>+S: setRimImage(image)
    M->>+S: setFaceImage(image)
    M->>+S: setTicksImage(image)

    M->>+S: setSpeed(speed)
    M->>+D: saveSpeedometerMetrics(metrics)
    M->>+N: syncWithOtherApps()

    M->>+A: animateSpeedometerView(speedometerView, metrics)
    A->>-M: animatedSpeedometerView

    M->>-S: speedometerView
    S->>-M: updatedSpeedometerView
```

## Anything Unclear
There are no unclear points.]

## Format example

---
## Required Swift third-party packages
```swift
"""
flask==1.1.2
bcrypt==3.2.0
"""
```

## Required Other language third-party packages
```swift
"""
No third-party ...
"""
```

## Full API spec
```swift
"""
openapi: 3.0.0
...
description: A JSON object ...
"""
```

## Logic Analysis
```swift
[
    ("game.swift", "Contains ..."),
]
```

## Task list
```swift
[
    "game.swift",
]
```

## Shared Knowledge
```swift
"""
'game.swift' contains ...
"""
```

## Anything Unclear
We need ... how to start.
---

-----
Role: You are a project manager; the goal is to break down tasks according to PRD/technical design, give a task list, and analyze task dependencies to start with the prerequisite modules
Requirements: Based on the context, fill in the following missing information, note that all sections are returned in Swift code triple quote form seperatedly. Here the granularity of the task is a file, if there are any missing files, you can supplement them
Attention: Use '##' to split sections, not '#', and '## <SECTION_NAME>' SHOULD WRITE BEFORE the code and triple quote.

## Required Swift third-party packages: Provided in requirements.txt format

## Required Other language third-party packages: Provided in requirements.txt format

## Full API spec: Use OpenAPI 3.0. Describe all APIs that may be used by both frontend and backend.

## Logic Analysis: Provided as a Python list[str, str]. the first is filename, the second is class/method/function should be implemented in this file. Analyze the dependencies between the files, which work should be done first

## Task list: Provided as Python list[str]. Each str is a filename, the more at the beginning, the more it is a prerequisite dependency, should be done first

## Shared Knowledge: Anything that should be public like utils' functions, config's variables details that should make clear first. 

## Anything Unclear Provide as Plain text. Make clear here. For example, don't forget a main entry. don't forget to init 3rd party libs.

