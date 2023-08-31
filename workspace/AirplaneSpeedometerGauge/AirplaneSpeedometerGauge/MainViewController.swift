import UIKit
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
