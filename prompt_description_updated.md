
**Role**:
You are a professional Swift engineer tasked with developing components for an aviation gauge widget tailored for iOS.

**Context**:
The primary goal is to develop a gauge widget for iOS applications tailored for aviation metrics. The widget should provide real-time representation of aviation metrics such as speed, ensure compatibility with iPad and iPhone devices, and have customizable visual elements.

**Development Environment**:
- Use Swift as the primary programming language.
- Utilize UIKit and SwiftUI for development components.

**Core Features**:
- Real-time representation of aviation metrics like speed.
- Customizable visual elements: rim appearance (`rimPaint`), speedometer face (`faceRect`), scale marks (`scaleTickPaint`, `scaleTextPaint`), color representation (`yellowScalePaint`, `greenScalePaint`, `redScalePaint`), speedometer hand (`handPaint`), and Yaw gauge hand (`handPaint`).

**Data Management**:
- Implement functionalities to adjust, save, and retrieve gauge metrics.
- Use SQLite.swift for persistent storage.

**Instructions**:
- Ensure your code adheres to the [Swift API Design Guidelines](https://swift.org/documentation/api-design-guidelines/), ensuring clarity and readability.
- Implement the code for the filename `MainView.swift`.
- Always use strong typing and explicit variable declarations.
- Follow the provided "Data Structures and Interface Definitions" without making changes to the design.

**Output**:
Provide the code for the filename `MainView.swift`. Ensure it's enclosed within triple quotes and follows the Swift syntax.

```swift
## MainView.swift
...
```

## Data Structures and Interface Definitions:

### Class Diagram:
```mermaid
classDiagram
    class MainView{
        +var gaugeView: GaugeView
        +func startTest()
        +func endTest()
    }

    class GaugeView{
        +var speedometer: Speedometer
        +var yawGauge: YawGauge
        +func customizeAppearance()
    }

    class Speedometer{
        +var speed: Double
        +func updateSpeed(newSpeed: Double)
    }

    class YawGauge{
        +var yaw: Double
        +func updateYaw(newYaw: Double)
    }

    class DataManager{
        +func adjustMetrics(metric: String, value: Double)
        +func saveMetrics()
        +func retrieveMetrics() -> [String: Double]
    }

    class NetworkManager{
        +func sendRequest(url: String, parameters: [String: Any], completion: (Result<Data, Error>) -> Void)
    }

    class DatabaseManager{
        +func createTable(tableName: String)
        +func insertData(tableName: String, data: [String: Any])
        +func updateData(tableName: String, data: [String: Any], condition: String)
        +func queryData(tableName: String, condition: String) -> [[String: Any]]
    }

    class TestManager{
        +func runTest()
        +func writeTestReport(report: TestReport)
    }

    class TestReport{
        +var testName: String
        +var testResult: String
        +var testDate: Date
    }

    class Utils{
        +static func formatSpeed(speed: Double) -> String
        +static func formatYaw(yaw: Double) -> String
    }

    MainView "1" -- "1" GaugeView: has
    GaugeView "1" -- "1" Speedometer: has
    GaugeView "1" -- "1" YawGauge: has
    DataManager "1" -- "1" NetworkManager: has
    DataManager "1" -- "1" DatabaseManager: has
    DataManager "1" -- "1" TestManager: has
    TestManager "1" -- "1" TestReport: has
```

### Program Call Flow:
```mermaid
sequenceDiagram
    participant M as MainView
    participant G as GaugeView
    participant D as DataManager
    participant N as NetworkManager
    participant DB as DatabaseManager
    participant TM as TestManager
    participant TR as TestReport
    participant U as Utils

    M->>G: startTest()
    G->>D: adjustMetrics(metric, value)
    D->>N: sendRequest(url, parameters)
    N-->>D: completion(result)
    D->>DB: insertData(tableName, data)
    D->>DB: queryData(tableName, condition)
    DB-->>D: data
    D->>TM: writeTestReport(report)
    TM->>TR: init(testName, testResult, testDate)
    TR-->>TM: report
    TM-->>M: report
    M->>G: endTest()
```
