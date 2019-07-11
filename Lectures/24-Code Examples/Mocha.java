public class Mocha extends CondimentDecorator {

  public Mocha(Beverage beverage) {
    super(beverage, "Mocha");
  }

  public double cost() {
    return .20 + getBeverage().cost();
  }

}
