# Your role
- World-class iOS Developer

# Your task
- Add "Run Complete" as a title to the dialog box and put a border around it so that it is positioned in the lower center of the dialog box instead of filling up the entire screen.
- The next row should have a label that says "Result"
- The next row should say: {percent_graviy} % g (replacing percent_gravity with the actual value)
- Above the dialog box, there should be a label called "Contaminate"

# Source code for the view controller
```swift
import UIKit

class RunCompleteViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    var resultValue: Float = 0.0  // This should be set before presenting the dialog
    var onAccept: (() -> Void)?
    
    private let contaminate = UILabel()
    private let optionsButton = UIButton()
    private let optionsTableView = UITableView()
    private let acceptButton = UIButton()
    private let rejectButton = UIButton()
    private let options = ["Loose Snow (LSR)", "Packed Snow (PSR)", "Ice (IR)", "Wet (WR)", "Slush (SLR)", "Patchy Ice (PIR)", "Patchy Slush (PSR)"]
    private var isDropdownVisible = false

    override func viewDidLoad() {
        super.viewDidLoad()
        setupViews()
    }

    private func setupViews() {
        view.backgroundColor = UIColor.white
        
        // Setup the accept button
        acceptButton.setTitle("Accept", for: .normal)
        acceptButton.backgroundColor = UIColor.blue
        acceptButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(acceptButton)

        // Setup the reject button
        rejectButton.setTitle("Reject", for: .normal)
        rejectButton.backgroundColor = UIColor.red
        rejectButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(rejectButton)

        // Setup the options button
        optionsButton.setTitle("Select Option", for: .normal)
        optionsButton.backgroundColor = UIColor.blue
        optionsButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(optionsButton)

        // Setup the options table view
        optionsTableView.isHidden = true
        optionsTableView.delegate = self
        optionsTableView.dataSource = self
        optionsTableView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(optionsTableView)

        

        // Constraints for options button
        NSLayoutConstraint.activate([
            optionsButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            optionsButton.centerYAnchor.constraint(equalTo: view.centerYAnchor, constant: -20),
            optionsButton.widthAnchor.constraint(equalToConstant: 200),
            optionsButton.heightAnchor.constraint(equalToConstant: 50)
        ])

        // Constraints for options table view
        NSLayoutConstraint.activate([
            optionsTableView.topAnchor.constraint(equalTo: optionsButton.bottomAnchor),
            optionsTableView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            optionsTableView.widthAnchor.constraint(equalToConstant: 200),
            optionsTableView.heightAnchor.constraint(equalToConstant: 175)  // Adjust as needed
        ])

        // Constraints for accept button
        NSLayoutConstraint.activate([
            acceptButton.topAnchor.constraint(equalTo: optionsTableView.bottomAnchor, constant: -120), // y-pos
            acceptButton.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 220),        // x-pos
            acceptButton.widthAnchor.constraint(equalToConstant: 100),
            acceptButton.heightAnchor.constraint(equalToConstant: 44)
        ])

        // Constraints for reject button
        NSLayoutConstraint.activate([
            rejectButton.topAnchor.constraint(equalTo: optionsTableView.bottomAnchor, constant: -120), // y-pos
            rejectButton.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -220),     // x-pos
            rejectButton.widthAnchor.constraint(equalToConstant: 100),
            rejectButton.heightAnchor.constraint(equalToConstant: 44)
        ])

        // Button action
        optionsButton.addTarget(self, action: #selector(toggleDropdown), for: .touchUpInside)
        acceptButton.addTarget(self, action: #selector(acceptPressed), for: .touchUpInside)
        rejectButton.addTarget(self, action: #selector(dismissDialog), for: .touchUpInside)
    }

    @objc private func toggleDropdown() {
        isDropdownVisible.toggle()
        optionsTableView.isHidden = !isDropdownVisible
    }

    @objc private func acceptPressed() {
        onAccept?()
        dismiss(animated: true, completion: nil)
    }

    @objc private func dismissDialog() {
        dismiss(animated: true, completion: nil)
    }

    // MARK: - UITableViewDelegate & UITableViewDataSource
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return options.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: .default, reuseIdentifier: "cell")
        cell.textLabel?.text = options[indexPath.row]
        return cell
    }

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        optionsButton.setTitle(options[indexPath.row], for: .normal)
        toggleDropdown()
    }
}
```