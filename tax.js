function r_n_d(taxable_income) {
  //level
    var lv = [0, 36000, 144000, 300000, 420000, 660000, 960000];
    //tax rate
    var r = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45];
    //quick deduction
    var d = [0, 2520, 16920, 31920, 52920, 85920, 181920];

    if (taxable_income <= lv[1])
    {
      tr = r[0] //tax_rate;
      qd = d[0] //quick_deduction;
      return [lv[0], tr, qd];
    }
    else if (taxable_income > lv[1] && taxable_income <= lv[2])
    {
      tr = r[1];
      qd = d[1];
      return [lv[1], tr, qd];
    }
    else if (taxable_income > lv[2] && taxable_income <= lv[3])
    {
      tr = r[2];
      qd = d[2];
      return [lv[2], tr, qd];
    }
    else if (taxable_income > lv[3] && taxable_income <= lv[4])
    {
      tr = r[3];
      qd = d[3];
      return [lv[3], tr, qd];
    }
    else if (taxable_income > lv[4] && taxable_income <= lv[5])
    {
      tr = r[4];
      qd = d[4];
      return [lv[4], tr, qd];
    }
    else if (taxable_income > lv[5] && taxable_income <= lv[6])
    {
      tr = r[5];
      qd = d[5];
      return [lv[5], tr, qd];
    }
    else{
      tr = r[6];
      qd = d[6];
      return [lv[6], tr, qd];
    }
}

function calculator(month, income, bonus, tax_free_income, security_n_fund, tax_threshold, special_deduction, other_deduction) {
  //根据月份，确定每月的累计应税额
    var taxable_income_by_month = [];
    var i = 0;
    while (i < month){
      i+=1;
      var current_taxable_income = (income - tax_free_income - security_n_fund - tax_threshold - special_deduction - other_deduction) * i;
      taxable_income_by_month.push(current_taxable_income);
    }

    //根据每月的累计应税所得额，找到相应的税率和速算扣除数，得到每月的应预扣预缴税额
    //这里假设了每月工资相同，所有的扣除项目也都相同
    var total_tax = [];
    var rate_by_month = [];
    var deduction_by_month = [];
    for (item in taxable_income_by_month){
      var current_rate = r_n_d(taxable_income_by_month[item])[1];
      rate_by_month.push(current_rate);
      var current_deduction = r_n_d(taxable_income_by_month[item])[2];
      deduction_by_month.push(current_deduction);
      var total_tax_item = taxable_income_by_month[item] * current_rate - current_deduction;
      total_tax.push(total_tax_item);
    }

    //本期应预扣预缴税额 = 最后一个月的累计应预扣预缴税额-上个月的累计应预扣预缴税额
    var paid_tax;
    var current_tax;
    if (total_tax.length > 1){
      paid_tax = total_tax[total_tax.length-2];
      current_tax = total_tax[total_tax.length-1]-paid_tax;
    }
    else{
      paid_tax = 0;
      current_tax = total_tax[total_tax.length-1];
    }
    //本期应预扣预缴税额最小为0
    if (current_tax < 0){
      current_tax = 0
    }
    //算上当月的奖金部分
    if (bonus > 0){
      var year_end_taxable_income = taxable_income_by_month[0]*12
      if (year_end_taxable_income < 0){
        year_end_taxable_income = 0;
      }
      year_end_taxable_income += bonus;
      var year_end_tax_rate = r_n_d(year_end_taxable_income)[1];
      var bonus_tax = bonus * year_end_tax_rate
      if (year_end_tax_rate > rate_by_month[rate_by_month.length-1]){
        flag = 1;
      }
      else{
        flag = 0;
      }
      taxable_income_by_month[taxable_income_by_month.length-1] += bonus;
      current_rate = r_n_d(taxable_income_by_month[taxable_income_by_month.length-1])[1];
      total_tax[total_tax.length-1] = taxable_income_by_month[taxable_income_by_month.length-1] * current_rate;
      current_tax = total_tax[total_tax.length-1] - paid_tax;
    }
    else {
      flag = 0;
      bonus_tax = 0;
    }
    return [Number(current_tax.toFixed(2)), flag, bonus_tax];
}
