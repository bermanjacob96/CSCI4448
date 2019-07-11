public class Soy extends CondimentDecorator {

  public Soy(Beverage beverage) {
    super(beverage, "Soy");
  }

  public double cost() {
    return .15 + getBeverage().cost();
  }

}
