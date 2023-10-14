# Your role
- Expert iOS developer

# Your task
- Analyze the code below and help me figure out why the entire screen is black now.  We only need the gauge to be black, the other part of the screen should be white.

## ViewController.swift
```swift
import UIKit
class ViewController: UIViewController {
    
    @IBOutlet weak var commentsTextView: UITextView!
    @IBOutlet weak var program_view:     UITextView!
    @IBOutlet weak var location_text:    UITextField!
    @IBOutlet weak var airport_name:     UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        if let textView = commentsTextView {
            textView.layer.borderWidth = 1.0
            commentsTextView.layer.borderColor = UIColor.black.cgColor }
        if let airport_text = airport_name {
            airport_text.layer.borderWidth = 1.0
            airport_name.layer.borderColor = UIColor.black.cgColor }

        if let location = location_text {
            location.layer.borderWidth = 1.0
            location_text.layer.borderColor = UIColor.black.cgColor }
        if let program = program_view {
            program.layer.borderWidth = 1.0
            program_view.layer.borderColor = UIColor.black.cgColor }
        self.view.backgroundColor = .white
        view.backgroundColor = UIColor.white
        print( "ViewController viewDidLoad called" )}}
```

## ScaleDrawer.swift
```swift
class ScaleDrawer {
    let SCALE_START_ANGLE: CGFloat = .pi - ( 0.5 )
    let SCALE_END_ANGLE: CGFloat =   2 * .pi  + ( 0.5 )
    let SCALE_LINE_WIDTH: CGFloat = 10
    let SCALE_RADIUS_OFFSET: CGFloat = 20
   
    let red = UIColor.red.cgColor // Colors
    let yellow = UIColor.yellow.cgColor
    let green = UIColor.green.cgColor

    let totalRange: CGFloat = 10 // Updated    // Define the ranges for each color
    let redRange: CGFloat = 1 // Updated
    let yellowRange: CGFloat = 1 // Updated
    let greenRange: CGFloat = 6 // Updated

    func drawScale(on context: CGContext, in rect: CGRect) {
        let center = CGPoint(x: rect.midX, y: rect.midY)
        let radius = min(rect.width, rect.height) / 2

        // Fill only the circular gauge area with black
        context.setFillColor(UIColor.black.cgColor)
        context.addArc(center: center, radius: radius, startAngle: 0, endAngle: 2 * .pi, clockwise: false)
        context.fillPath()
        context.setLineWidth(SCALE_LINE_WIDTH)

        // Calculate the angle for each color range
        let redAngle = (redRange / totalRange) * (SCALE_END_ANGLE - SCALE_START_ANGLE)
        let yellowAngle = (yellowRange / totalRange) * (SCALE_END_ANGLE - SCALE_START_ANGLE)
        let greenAngle = (greenRange / totalRange) * (SCALE_END_ANGLE - SCALE_START_ANGLE)

        // Calculate the start and end angles for each color
        let redStartAngle = SCALE_START_ANGLE // Red starts at the beginning
        let redEndAngle = redStartAngle + redAngle
        let yellowStartAngle = redEndAngle
        let yellowEndAngle = yellowStartAngle + yellowAngle
        let greenStartAngle = yellowEndAngle
        let greenEndAngle = greenStartAngle + greenAngle
        let secondYellowStartAngle = greenEndAngle
        let secondYellowEndAngle = secondYellowStartAngle + yellowAngle
        let secondRedStartAngle = secondYellowEndAngle
        let secondRedEndAngle = SCALE_END_ANGLE // Red ends at the end

       
        context.setStrokeColor(red) // Red                                    // Draw the 
        context.addArc(center: center, radius: radius - SCALE_RADIUS_OFFSET,  // colored scales
                       startAngle: redStartAngle,
                       endAngle: redEndAngle,
                       clockwise: false)
        context.strokePath()

        context.setStrokeColor(yellow) // Yellow
        context.addArc(center: center, radius: radius - SCALE_RADIUS_OFFSET,
                       startAngle: yellowStartAngle,
                       endAngle: yellowEndAngle,
                       clockwise: false)
        context.strokePath()

        context.setStrokeColor(green)  // Green
        context.addArc(center: center, radius: radius - SCALE_RADIUS_OFFSET,
                       startAngle: greenStartAngle,
                       endAngle: greenEndAngle,
                       clockwise: false)
        context.strokePath()

        context.setStrokeColor(yellow) // Second Yellow
        context.addArc(center: center, radius: radius - SCALE_RADIUS_OFFSET,
                       startAngle: secondYellowStartAngle,
                       endAngle: secondYellowEndAngle,
                       clockwise: false)
        context.strokePath()

        context.setStrokeColor(red) // Second Red
        context.addArc(center: center, radius: radius - SCALE_RADIUS_OFFSET,
                       startAngle: secondRedStartAngle,
                       endAngle: secondRedEndAngle,
                       clockwise: false)
        context.strokePath()}}
```

## SpeedScaleView
```swift
import UIKit

class SpeedScaleView: UIView {
    lazy var speed: CGFloat = SpeedometerConfiguration.initialSpeed {
        didSet { self.speedometerNeedle.speed = speed; self.setNeedsDisplay()}}
    let yawGaugeDrawer = YawGaugeDrawer()
    let scaleDrawer = ScaleDrawer()
    lazy var speedometerNeedle = SpeedometerNeedle(speed: self.speed, SCALE_DIVISIONS: SpeedometerConfiguration.scaleDivisions, SCALE_START_ANGLE: SpeedometerConfiguration.scaleStartAngle, SCALE_END_ANGLE: SpeedometerConfiguration.scaleEndAngle)
    lazy var yawIndicator = YawIndicator(frame: CGRect(x: 0, y: 0, width: self.bounds.width, height: self.bounds.height))
    
    let tickMarkDrawer = TickMarkDrawer(
            scaleDivisions: SpeedometerConfiguration.scaleDivisions,
            tickRadiusOffset: SpeedometerConfiguration.tickRadiusOffset,
            tickMarkLength: SpeedometerConfiguration.tickMarkLength,
            tickMarkWidth: SpeedometerConfiguration.tickMarkWidth,
            textMargin: SpeedometerConfiguration.textMargin,
            textOffset: SpeedometerConfiguration.textOffset,
            textWidth: SpeedometerConfiguration.textWidth,
            textHeight: SpeedometerConfiguration.textHeight,
            currentScale: SpeedometerConfiguration.currentScale,
            offsetDegree: SpeedometerConfiguration.offsetDegree,
            stepDegree: SpeedometerConfiguration.stepDegree,
            scaleStartAngle: SpeedometerConfiguration.scaleStartAngle,
            scaleEndAngle:   SpeedometerConfiguration.scaleEndAngle,
            minorTickMarkLength: SpeedometerConfiguration.minorTickMarkLength )

    func valueForDivision( _ division: CGFloat ) -> Int {
        let totalDivisions = SpeedometerConfiguration.scaleDivisions * 2 // From -SCALE_DIVISIONS to SCALE_DIVISIONS
        let value = (division / totalDivisions) * 200 - 100 // This will give values from -100 to 100
        return Int( value )}

    override func draw(_ rect: CGRect) {
        self.addSubview(yawIndicator)  // Add the yaw indicator to the view hierarchy
        guard let context = UIGraphicsGetCurrentContext() else { return }
        context.setLineWidth( SpeedometerConfiguration.scaleLineWidth )
       
        scaleDrawer.drawScale(          on: context, in: rect   )  // Draw colors
        
        yawGaugeDrawer.drawYawGauge(    on: context, in: rect   )  // Draw the Yaw Gauge

        tickMarkDrawer.drawTickMarks(   on: context, in: rect   )  /* Draw tick marks*/
        speedometerNeedle.draw(         on: context, rect: rect )  // Draw the needle
        /* print ( "done with draw function" ) */ }}
```

## SpeedScaleViewController
```swift
class SpeedScaleViewController: UIViewController {
    private var variable: Float = -2.0
    private var timer: Timer?
    private var speedScaleView: SpeedScaleView!
    private var converter: RcrConverter!
    // create a file variable for the file test_data.txt and initialize it to test_data.txt
    private var test_data_file: FileHandle? = FileHandle(forReadingAtPath: "/Users/clay/Desktop/AirportNAC/Airport_Project/User_Interfaces/View_Controllers/test_data.txt" )
    private var test_data_array: [String] = []
    private var test_data_index: Int = 0
    @IBOutlet weak var speed: UITextField!
    @IBAction func sliderValueChanged( _ sender: UISlider ) {
        let sliderSpeed = sender.value  // This will be a value between -100 and 100 
        print("Slider value changed to: \(sliderSpeed)")
        speed.text = String( sliderSpeed )
        speedScaleView.speed = CGFloat( sliderSpeed )
        updateYawIndicator( yawValue: CGFloat( sliderSpeed ))
        // convertedSpeed.text = String( converter.convert( sliderSpeed: Int( sliderSpeed )))
    } // set the speed of the SpeedScaleView
    // pass in the yaw value to the yawIndicator
    func updateYawIndicator( yawValue: CGFloat ) {
        speedScaleView.yawIndicator.moveIndicator(toYaw: yawValue )
    }

    override func viewDidLoad() {
        print("SpeedScaleViewController viewDidLoad called")
        super.viewDidLoad()
        view.backgroundColor = UIColor.white   // Initialize the SpeedScaleView and add it to the view hierarchy
        speedScaleView = SpeedScaleView(frame: view.bounds)
        speedScaleView.backgroundColor = .black
        view.insertSubview(speedScaleView, at: 0)
        let desiredLeadingPadding: CGFloat = -200.0 // Adjust this value as needed
        speedScaleView.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            speedScaleView.topAnchor.constraint(equalTo: view.topAnchor),
            speedScaleView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            speedScaleView.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: desiredLeadingPadding),
            speedScaleView.trailingAnchor.constraint(equalTo: view.trailingAnchor)
        ])
        speedScaleView.speed = 0
        self.converter = RcrConverter()
        startUpdatingVariable()
        if self.test_data_file != nil {
            let data = test_data_file?.readDataToEndOfFile()
            let dataString = String(data: data!, encoding: .utf8)
            test_data_array = dataString!.components(separatedBy: "\n")
            test_data_file?.closeFile()
        }
    }
    
    func startUpdatingVariable() {
            timer?.invalidate() // Invalidate any existing timer
        speedScaleView.speed = -100 // Set the initial speed to -100
        timer = Timer.scheduledTimer(withTimeInterval: 0.15, repeats: true) { [weak self] _ in
                guard let self = self else { return }
            if ( self.test_data_index >= self.test_data_array.count ) {
                return
            }
            if self.speedScaleView.speed < 100 {
                let test_data = self.test_data_array[ self.test_data_index ]
                var xValue = ""
                var yValue = ""
                let regexPattern = "x: (-?\\d+\\.\\d+) y: (-?\\d+\\.\\d+)"
                if let regex = try? NSRegularExpression(pattern: regexPattern) {
                    let nsString = test_data as NSString
                    if let match = regex.firstMatch(in: test_data, range: NSRange(location: 0, length: nsString.length)) {
                        xValue = nsString.substring(with: match.range(at: 1))
                        yValue = nsString.substring(with: match.range(at: 2))
                        if let x = Double(xValue), let y = Double(yValue) {
                            print("x: \(x), y: \(y)")  // x: -0.0032, y: 0.0088
                        } else {
                            print("Failed to convert extracted values to Double.")
                        }
                    } else {
                        print("No match found.")
                    }
                } else {
                    print("Failed to create regex.")
                }
                
                if let xValueDouble = Double(xValue) {
                    self.speedScaleView.speed = CGFloat(xValueDouble * 100 )
                } else {
                    print("Failed to convert \(xValue) to Double.")
                }
                
                if let yValueDouble = Double(yValue) {
                    self.updateYawIndicator( yawValue: CGFloat( yValueDouble * 100 ))
                } else {
                    print("Failed to convert \(yValue) to Double.")
                }
                
                self.test_data_index = self.test_data_index + 1
            } else {
                self.timer?.invalidate() // Stop when the speed reaches 100
            }
        }
    }                 
    deinit { timer?.invalidate()}}
```