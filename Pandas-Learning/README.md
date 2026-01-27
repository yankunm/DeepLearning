# Things Need to Learn

## Load the dataset
- pd.read_csv()

## Inspect the dataset
- df.head()
- df.info()
- df.describe()

## Select columns
- df['target']
- df[['feature1', 'feature2']]

## Handle missing values (if any)
- df.dropna()
- df.fillna()

## Convert to NumPy
- df.to_numpy()
- df.values

# NumPy

## Basic array handling
- np.array()
- shape

## Build design matrix
- np.ones((N, 1))
- np.column_stack()

## Linear regression (analytical solution)
- np.linalg.lstsq()

## Matrix multiplication
- @

## Prediction
- X @ w

