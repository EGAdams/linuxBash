# Persona
- Expert iOS Developer

# Goal
- Analyze the view controller below and identify the issues that may cause a it to create a blank screen.
- Rewrite the view controller below and liberally place print statements to help debug the issue.


# Source
```swift
import UIKit

struct EvaluationItem {
    var title: String
    var description: String
    var date: Date
}

class DebugReviewViewController: UIViewController, UICollectionViewDelegate, UICollectionViewDataSource {

    var testsCollectionView: UICollectionView!
    var mockEvaluationItems: [EvaluationItem]!
    var dataSource: ProgramDataSource!

    var programCount: Int = 0

    static func start(context: UIViewController, programCount: Int, requestCode: Int) {
        let intent = DebugReviewViewController()
        intent.programCount = programCount
        context.present(intent, animated: true, completion: nil)
    }

    func generateMockEvaluationItemData(count: Int) -> [EvaluationItem] {
        var evaluationItems = [EvaluationItem]()
        for _ in 0..<count {
            let item = EvaluationItem(
                title: "Evaluation \(Int.random(in: 1...100))",
                description: "Description for evaluation",
                date: Date()
            )
            evaluationItems.append(item)
        }
        return evaluationItems
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        print("Debug: viewDidLoad called")

        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = .horizontal
        testsCollectionView = UICollectionView(frame: self.view.bounds, collectionViewLayout: layout)
        testsCollectionView.delegate = self
        testsCollectionView.dataSource = self
        testsCollectionView.register(TestCell.self, forCellWithReuseIdentifier: "TestCell")
        self.view.addSubview(testsCollectionView)

        print("Debug: CollectionView initialized with frame: \(self.view.bounds)")

        dataSource = ProgramDataSource()
        dataSource.open()
        updateProgramList(programCount: programCount)
        
        mockEvaluationItems = generateMockEvaluationItemData(count: 5)
        print("Debug: Mock evaluation items generated: \(mockEvaluationItems.count)")
    }

    func updateProgramList(programCount: Int) {
        print("Debug: updateProgramList called with programCount: \(programCount)")
        testsCollectionView.reloadData()
    }

    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        print("Debug: CollectionView numberOfItemsInSection called")
        return mockEvaluationItems.count
    }

    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        print("Debug: CollectionView cellForItemAt called for indexPath: \(indexPath)")
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "TestCell", for: indexPath) as! TestCell
        let test = mockEvaluationItems[indexPath.row]
        cell.configure(with: test)
        return cell
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        print("Debug: viewWillAppear called")
        dataSource.open()
        testsCollectionView.reloadData()
    }

    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        print("Debug: viewWillDisappear called")
        dataSource.close()
    }
}

class TestCell: UICollectionViewCell {
    func configure(with evaluationItem: EvaluationItem) {
        // Configure the cell's UI elements with data from the test instance
    }
}

class ProgramDataSource {
    func open() {}
    func close() {}
    func numberOfTests() -> Int {
        return 10
    }
}

class TestsCursorAdapter {
    // Implementation for tests cursor adapter
}
```
