SELECT S.Name FROM Students AS S, Friends AS F, Packages AS PS, Packages AS PF 
WHERE S.ID = F.ID AND F.ID = PS.ID AND F.Friend_ID = PF.ID
   AND PS.Salary < PF.Salary
ORDER BY PF.Salary
