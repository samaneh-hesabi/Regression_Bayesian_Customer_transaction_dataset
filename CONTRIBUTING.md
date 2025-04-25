<div style="font-size:2.5em; font-weight:bold; text-align:center; margin-top:20px;">Contributing Guidelines</div>

## 1. Getting Started
1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/Regression_Bayesian_Customer_transaction_dataset.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

## 1.1 Development Workflow
1. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes
3. Run tests: `pytest`
4. Format code: `black .`
5. Check for linting errors: `flake8`
6. Commit your changes with a descriptive message:
   ```bash
   git commit -m "feat: add new feature"  # for new features
   git commit -m "fix: resolve bug"       # for bug fixes
   git commit -m "docs: update documentation"  # for documentation
   ```
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request

## 1.2 Code Style
- Follow PEP 8 guidelines
- Use type hints for function parameters and return values
- Write docstrings for all functions and classes
- Keep functions focused and single-purpose
- Use meaningful variable and function names

## 1.3 Testing
- Write unit tests for new features
- Ensure all tests pass before submitting a PR
- Add integration tests for complex features
- Maintain test coverage above 80%

## 1.4 Documentation
- Update README.md for significant changes
- Add docstrings to new functions and classes
- Include examples in docstrings where appropriate
- Update type hints when modifying function signatures

## 1.5 Pull Request Process
1. Ensure your PR description clearly explains the changes
2. Reference any related issues
3. Wait for review and address any feedback
4. Once approved, squash and merge your PR

## 1.6 Questions?
If you have any questions, please open an issue in the repository. 