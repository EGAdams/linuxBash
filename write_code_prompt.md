
NOTICE
Role: You are a professional engineer; the main goal is to write PEP8 compliant, elegant, modular, easy to read and maintain Swift code.
ATTENTION: Use '##' to SPLIT SECTIONS, not '#'. Output format carefully referenced "Format example".

## Code: NetworkHelper.swift Write code with triple quoto, based on the following list and context.
1. Do your best to implement THIS ONLY ONE FILE. ONLY USE EXISTING API. IF NO API, IMPLEMENT IT.
2. Requirement: Based on the context, implement one following code file, note to return only in code form, your code will be part of the entire project, so please implement complete, reliable, reusable code snippets
3. Attention1: If there is any setting, ALWAYS SET A DEFAULT VALUE, ALWAYS USE STRONG TYPE AND EXPLICIT VARIABLE.
4. Attention2: YOU MUST FOLLOW "Data Structures and Interface Definitions". DONT CHANGE ANY DESIGN.
5. Think before writing: What should be implemented and provided in this document?
6. CAREFULLY CHECK THAT YOU DONT MISS ANY NECESSARY CLASS/FUNCTION IN THIS FILE.
7. Do not use public member functions that do not exist in your design.

-----
# Context
[BOSS: Develop an iOS application for iPad and iPhone that functions as an airplane speedometer gauge. Use Swift and UIKit for the main development. Ensure real-time representation of speed, yaw, and other metrics. Incorporate customizable visual elements (rim, face, ticks) and leverage Core Animation for smooth visual transitions. Implement functionalities to adjust, save, and retrieve gauge metrics using Core Data. Prioritize compatibility across iOS devices and ensure an intuitive user experience. Provide synchronization capabilities with other aviation-related iOS applications., Product Manager: ## Original Requirements:
[BOSS: Develop an iOS application for iPad and iPhone that functions as an airplane speedometer gauge. Use Swift and UIKit for the main development. Ensure real-time representation of speed, yaw, and other metrics. Incorporate customizable visual elements (rim, face, ticks) and leverage Core Animation for smooth visual transitions. Implement functionalities to adjust, save, and retrieve gauge metrics using Core Data. Prioritize compatibility across iOS devices and ensure an intuitive user experience. Provide synchronization capabilities with other aviation-related iOS applications.]

## Product Goals:
```python
[
    "Create a high-quality airplane speedometer gauge application for iOS devices",
    "Ensure real-time representation of speed, yaw, and other metrics",
    "Provide customization options for visual elements and smooth visual transitions"
]
```

## User Stories:
```python
[
    "As a pilot, I want to have a reliable speedometer gauge on my iOS device to monitor my airplane's speed and other metrics in real-time.",
    "As a user, I want to be able to customize the visual elements of the speedometer gauge, such as the rim, face, and ticks, to suit my personal preferences.",
    "As a user, I want the speedometer gauge to have smooth visual transitions and animations for a more enjoyable user experience.",
    "As a pilot, I want to be able to adjust, save, and retrieve gauge metrics using Core Data for easy access and management.",
    "As a user, I want the speedometer gauge to be compatible with different iOS devices, including iPad and iPhone, for flexibility in usage."
]
```

## Competitive Analysis:
```python
[
    "Air Speedometer Pro: A popular airplane speedometer gauge application for iOS devices with customizable visual elements and real-time representation of speed and other metrics.",
    "Flight Instruments: An aviation-related iOS application that provides a comprehensive set of flight instruments, including a speedometer gauge, for pilots.",
    "Aviation Speedometer: An iOS application specifically designed for aviation enthusiasts, offering a speedometer gauge with customizable visual elements and synchronization capabilities with other aviation-related apps.",
    "Speed Gauge Pro: A feature-rich speedometer gauge application for iOS devices, offering real-time speed representation, customizable visual elements, and smooth visual transitions.",
    "Flight Companion: An iOS application that provides various aviation-related tools and features, including a speedometer gauge, for pilots.",
    "Aviation Toolkit: A comprehensive toolkit for aviation enthusiasts, including a speedometer gauge with real-time speed representation and customizable visual elements.",
    "Pilot Speedometer: An iOS application designed for pilots, offering a speedometer gauge with real-time speed representation and synchronization capabilities with other aviation-related apps."
]
```

## Competitive Quadrant Chart:
```mermaid
quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    "Air Speedometer Pro": [0.7, 0.8]
    "Flight Instruments": [0.6, 0.7]
    "Aviation Speedometer": [0.8, 0.6]
    "Speed Gauge Pro": [0.7, 0.7]
    "Flight Companion": [0.5, 0.6]
    "Aviation Toolkit": [0.6, 0.5]
    "Pilot Speedometer": [0.7, 0.7]
    "Our Target Product": [0.6, 0.7]
```

## Requirement Analysis:
The product should be an iOS application for iPad and iPhone that functions as an airplane speedometer gauge. It should provide real-time representation of speed, yaw, and other metrics. The application should incorporate customizable visual elements, such as the rim, face, and ticks, and leverage Core Animation for smooth visual transitions. It should also implement functionalities to adjust, save, and retrieve gauge metrics using Core Data. The application should prioritize compatibility across iOS devices and ensure an intuitive user experience. Additionally, it should provide synchronization capabilities with other aviation-related iOS applications.

## Requirement Pool:
```python
[
    ("Implement a real-time representation of yaw and other metrics", "P0"),
    ("Add customization options for visual elements (rim, face, ticks)", "P1"),
    ("Leverage Core Animation for smooth visual transitions", "P1"),
    ("Implement functionalities to adjust, save, and retrieve gauge metrics using Core Data", "P0"),
    ("Ensure compatibility across iOS devices (iPad and iPhone)", "P0")
]
```

## UI Design draft:
The speedometer gauge application will have a clean and intuitive user interface. It will consist of a circular gauge with a customizable rim, face, and ticks. The gauge will display the current speed and other metrics in real-time. Users will be able to adjust the gauge metrics using intuitive controls. The application will also provide options to save and retrieve gauge metrics using Core Data. Smooth visual transitions and animations will be implemented using Core Animation. The design will prioritize compatibility across iOS devices, ensuring a consistent user experience on both iPad and iPhone.

## Anything Unclear:
There are no unclear points., Architect: ## Implementation approach
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
There are no unclear points., Project Manager: ## Required Swift third-party packages:
```swift
"""
SwiftSVG
SVGKit
Lottie
CoreDataKit
MagicalRecord
SnapKit
PureLayout
Alamofire
SwiftyJSON
"""
```

## Required Other language third-party packages:
```swift
"""
No third-party packages required for other languages.
"""
```

## Full API spec:
```swift
"""
openapi: 3.0.0
info:
  title: Airplane Speedometer Gauge API
  description: API for syncing airplane speedometer gauge data with other aviation-related applications
  version: 1.0.0
servers:
  - url: https://api.example.com
paths:
  /metrics:
    get:
      summary: Retrieve speedometer metrics
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  speed:
                    type: integer
                    description: The current speed in km/h
                  yaw:
                    type: integer
                    description: The yaw angle in degrees
                  otherMetrics:
                    type: integer
                    description: Other relevant metrics
    post:
      summary: Save speedometer metrics
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                speed:
                  type: integer
                  description: The current speed in km/h
                yaw:
                  type: integer
                  description: The yaw angle in degrees
                otherMetrics:
                  type: integer
                  description: Other relevant metrics
      responses:
        '200':
          description: Successful response
        '400':
          description: Invalid request
  /sync:
    post:
      summary: Sync speedometer metrics with other aviation-related applications
      responses:
        '200':
          description: Successful response
        '400':
          description: Invalid request
"""
```

## Logic Analysis:
```swift
[
    ("MainViewController.swift", "MainViewController.viewDidLoad()"),
    ("SpeedometerView.swift", "SpeedometerView.setSpeed(int)"),
    ("SpeedometerView.swift", "SpeedometerView.setRimImage(UIImage)"),
    ("SpeedometerView.swift", "SpeedometerView.setFaceImage(UIImage)"),
    ("SpeedometerView.swift", "SpeedometerView.setTicksImage(UIImage)"),
    ("CustomizationViewController.swift", "CustomizationViewController.viewDidLoad()"),
    ("DataStorageManager.swift", "DataStorageManager.saveMetrics(SpeedometerMetrics)"),
    ("DataStorageManager.swift", "DataStorageManager.retrieveMetrics()"),
    ("NetworkingManager.swift", "NetworkingManager.syncWithOtherApps()"),
    ("AnimationHelper.swift", "AnimationHelper.animateSpeedometerView(SpeedometerView, SpeedometerMetrics)"),
    ("LocationHelper.swift", "LocationHelper.startUpdatingLocation()"),
    ("LocationHelper.swift", "LocationHelper.getCurrentSpeed()"),
    ("UserDefaultsHelper.swift", "UserDefaultsHelper.saveObject(Any, String)"),
    ("UserDefaultsHelper.swift", "UserDefaultsHelper.retrieveObject(String)"),
    ("NetworkHelper.swift", "NetworkHelper.sendRequest(URL, [String: Any], (Data?, Error?) -> Void)"),
    ("NetworkHelper.swift", "NetworkHelper.parseResponse(Data) -> [String: Any]")
]
```

## Task list:
```swift
[
    "MainViewController.swift",
    "SpeedometerView.swift",
    "CustomizationViewController.swift",
    "DataStorageManager.swift",
    "NetworkingManager.swift",
    "AnimationHelper.swift",
    "LocationHelper.swift",
    "UserDefaultsHelper.swift",
    "NetworkHelper.swift"
]
```

## Shared Knowledge:
```swift
"""
The 'game.swift' file contains the implementation for the game logic and should be implemented after the other files are completed.
"""
```

## Anything Unclear:
There are no unclear points., Engineer: import UIKit
import CoreLocation

class MainViewController: UIViewController {
    private var speedometerView: SpeedometerView!
    private var customizationViewController: CustomizationViewController!
    private var dataStorageManager: DataStorageManager!
    private var networkingManager: NetworkingManager!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        speedometerView = SpeedometerView()
        customizationViewController = CustomizationViewController()
        dataStorageManager = DataStorageManager()
        networkingManager = NetworkingManager()
        
        setupSpeedometerView()
        setupCustomizationViewController()
        
        startUpdatingLocation()
    }
    
    private func setupSpeedometerView() {
        speedometerView.delegate = self
        view.addSubview(speedometerView)
        
        // Add constraints to position and size the speedometer view
    }
    
    private func setupCustomizationViewController() {
        customizationViewController.delegate = self
        // Add customization view controller as a child view controller
        
        // Add constraints to position and size the customization view controller
    }
    
    private func startUpdatingLocation() {
        LocationHelper.shared.startUpdatingLocation()
    }
    
    private func stopUpdatingLocation() {
        LocationHelper.shared.stopUpdatingLocation()
    }
    
    private func updateSpeedometerMetrics(metrics: SpeedometerMetrics) {
        speedometerView.setSpeed(metrics.speed)
    }
    
    private func saveSpeedometerMetrics(metrics: SpeedometerMetrics) {
        dataStorageManager.saveMetrics(metrics)
    }
    
    private func retrieveSpeedometerMetrics() -> SpeedometerMetrics {
        return dataStorageManager.retrieveMetrics()
    }
    
    private func syncWithOtherApps() {
        networkingManager.syncWithOtherApps()
    }
}

extension MainViewController: SpeedometerViewDelegate {
    func speedometerViewDidTapCustomizeButton() {
        // Show customization view controller
    }
}

extension MainViewController: CustomizationViewControllerDelegate {
    func customizationViewControllerDidSaveOptions() {
        // Save customization options
    }
}
, Engineer: import UIKit

class SpeedometerView: UIView {
    private var rimImageView: UIImageView!
    private var faceImageView: UIImageView!
    private var ticksImageView: UIImageView!
    private var speedLabel: UILabel!
    
    func setSpeed(_ speed: Int) {
        speedLabel.text = "\(speed) km/h"
    }
    
    func setRimImage(_ image: UIImage) {
        rimImageView.image = image
    }
    
    func setFaceImage(_ image: UIImage) {
        faceImageView.image = image
    }
    
    func setTicksImage(_ image: UIImage) {
        ticksImageView.image = image
    }
}
, Engineer: import UIKit

class CustomizationViewController: UIViewController {
    private var customizationOptionsTableView: UITableView!
    private var customizationOptions: [CustomizationOption] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        customizationOptionsTableView = UITableView()
        customizationOptionsTableView.delegate = self
        customizationOptionsTableView.dataSource = self
        view.addSubview(customizationOptionsTableView)
        
        // Add constraints to position and size the table view
    }
    
    private func loadCustomizationOptions() {
        // Load customization options from a JSON file or other data source
        // and populate the customizationOptions array
    }
    
    private func saveCustomizationOptions() {
        // Save customization options to a JSON file or other data source
    }
}

extension CustomizationViewController: UITableViewDelegate, UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return customizationOptions.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "CustomizationOptionCell", for: indexPath)
        
        let option = customizationOptions[indexPath.row]
        cell.textLabel?.text = option.title
        
        return cell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let option = customizationOptions[indexPath.row]
        // Handle option selection
    }
}
, Engineer: import UIKit
import CoreData

class DataStorageManager {
    private let context: NSManagedObjectContext
    
    init() {
        guard let appDelegate = UIApplication.shared.delegate as? AppDelegate else {
            fatalError("Unable to access AppDelegate")
        }
        context = appDelegate.persistentContainer.viewContext
    }
    
    func saveMetrics(_ metrics: SpeedometerMetrics) {
        let entity = NSEntityDescription.entity(forEntityName: "Metrics", in: context)!
        let metricsObject = NSManagedObject(entity: entity, insertInto: context)
        
        metricsObject.setValue(metrics.speed, forKey: "speed")
        metricsObject.setValue(metrics.yaw, forKey: "yaw")
        metricsObject.setValue(metrics.otherMetrics, forKey: "otherMetrics")
        
        do {
            try context.save()
        } catch {
            print("Failed to save metrics: \(error)")
        }
    }
    
    func retrieveMetrics() -> SpeedometerMetrics {
        let fetchRequest = NSFetchRequest<NSFetchRequestResult>(entityName: "Metrics")
        
        do {
            let result = try context.fetch(fetchRequest)
            if let metricsObject = result.first as? NSManagedObject {
                let speed = metricsObject.value(forKey: "speed") as? Int ?? 0
                let yaw = metricsObject.value(forKey: "yaw") as? Int ?? 0
                let otherMetrics = metricsObject.value(forKey: "otherMetrics") as? Int ?? 0
                
                return SpeedometerMetrics(speed: speed, yaw: yaw, otherMetrics: otherMetrics)
            }
        } catch {
            print("Failed to retrieve metrics: \(error)")
        }
        
        return SpeedometerMetrics(speed: 0, yaw: 0, otherMetrics: 0)
    }
}
, Engineer: import UIKit
import Alamofire
import SwiftyJSON

class NetworkingManager {
    private let baseURL = "https://api.example.com"
    
    func syncWithOtherApps() {
        guard let url = URL(string: "\(baseURL)/sync") else {
            print("Invalid URL")
            return
        }
        
        let parameters: [String: Any] = [
            // Add parameters for synchronization
        ]
        
        sendRequest(url: url, parameters: parameters) { data, error in
            if let error = error {
                print("Error: \(error)")
                return
            }
            
            guard let data = data else {
                print("No data received")
                return
            }
            
            let response = self.parseResponse(data: data)
            // Process response data
        }
    }
    
    private func sendRequest(url: URL, parameters: [String: Any], completion: @escaping (Data?, Error?) -> Void) {
        Alamofire.request(url, method: .post, parameters: parameters, encoding: JSONEncoding.default)
            .validate()
            .responseData { response in
                switch response.result {
                case .success(let data):
                    completion(data, nil)
                case .failure(let error):
                    completion(nil, error)
                }
            }
    }
    
    private func parseResponse(data: Data) -> [String: Any] {
        do {
            let json = try JSON(data: data)
            return json.dictionaryObject ?? [:]
        } catch {
            print("Failed to parse response: \(error)")
            return [:]
        }
    }
}
, Engineer: import UIKit

class AnimationHelper {
    static func animateSpeedometerView(speedometerView: SpeedometerView, metrics: SpeedometerMetrics) {
        UIView.animate(withDuration: 0.5) {
            speedometerView.setSpeed(metrics.speed)
            // Animate other properties of the speedometer view based on the metrics
        }
    }
}
, Engineer: import UIKit
import CoreLocation

class LocationHelper: NSObject, CLLocationManagerDelegate {
    static let shared = LocationHelper()
    
    private let locationManager = CLLocationManager()
    
    private override init() {
        super.init()
        
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
    }
    
    func startUpdatingLocation() {
        locationManager.requestWhenInUseAuthorization()
        locationManager.startUpdatingLocation()
    }
    
    func stopUpdatingLocation() {
        locationManager.stopUpdatingLocation()
    }
    
    func getCurrentLocation() -> CLLocationCoordinate2D? {
        return locationManager.location?.coordinate
    }
    
    func getCurrentSpeed() -> Double {
        return locationManager.location?.speed ?? 0.0
    }
    
    // MARK: - CLLocationManagerDelegate
    
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        if status == .authorizedWhenInUse {
            locationManager.startUpdatingLocation()
        }
    }
}
, Engineer: import Foundation

class UserDefaultsHelper {
    static func saveObject(object: Any, forKey: String) {
        UserDefaults.standard.set(object, forKey: forKey)
    }
    
    static func retrieveObject(forKey: String) -> Any? {
        return UserDefaults.standard.object(forKey: forKey)
    }
}
]
-----
## Format example
-----
## Code: NetworkHelper.swift
```swift
## NetworkHelper.swift
...
```
-----
