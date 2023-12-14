"use client";

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { OFFICIAL_RATES } from "@/constants";
import { zodResolver } from "@hookform/resolvers/zod";
import { ArrowSwapHorizontal, BitcoinRefresh } from "iconsax-react";
import { useRouter } from "next/navigation";
import { useForm } from "react-hook-form";
import * as z from "zod";
<<<<<<< HEAD
import isAuth from "@/components/isAuth";
import axios from "axios";
import { getCoinList, sellRoute } from "@/lib/helpers";
import { getCookie } from "@/lib/utils";
import { useEffect, useState } from "react";
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area";
=======
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c

const formSchema = z.object({
  bankName: z.string().min(1, { message: "Please provide your bank name" }),
  accountNumber: z
    .string()
    .min(1, { message: "Please provide your account number" }),
  coinType: z.string().min(1, {
    message: "Coin type is required",
  }),
  amount: z.coerce.number().min(0, { message: "Amount cannot be negative" }),
});

<<<<<<< HEAD
const Sellpage = () => {
  const router = useRouter();
  const [enteredAmount, setEnteredAmount] = useState<number | undefined>(
    undefined
  );
  const [coinlist, setCoinList] = useState<any[]>([]);
=======
const onPaste = () => {
  navigator.clipboard.readText().then((text) => {
    if (text) {
      formSchema.parse(text);
    }
  });
};

const Sellpage = () => {
  const router = useRouter();
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      coinType: "",
      bankName: "",
      accountNumber: "",
      amount: 0,
    },
  });
<<<<<<< HEAD

  const accessToken = getCookie("access_token");

  useEffect(() => {
    const fetchCoinData = async () => {
      try {
        const response = await axios.get(getCoinList);
        const coinList = response.data;
        setCoinList(coinList);
      } catch (error) {
        console.error("Error", error);
      }
    };

    fetchCoinData();
  }, [form]);

  const onSubmit = async (data: z.infer<typeof formSchema>) => {
    router.push("/dashboard/transactions/buy&sell/sell/sell_confirmation");
  };
=======
  const onSubmit = (data: z.infer<typeof formSchema>) => {};
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
  return (
    <div className="flex justify-center flex-col space-y-8 items-center py-12">
      <p className="text-primary font-medium min-[450px]:text-left text-center ">
        Kindly provide your bank number and account number
      </p>
      <Card className="bg-transparent border-none shadow-none w-[400px]">
        <CardContent className="py-2">
          <Form {...form}>
            <form
              className="space-y-10 min-[450px]:p-0 px-6"
              onSubmit={form.handleSubmit(onSubmit)}
            >
              <FormField
                control={form.control}
                name="coinType"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel className="font-normal text-primary text-base">
                      Coin Type
                    </FormLabel>
                    <Select
                      onValueChange={field.onChange}
                      defaultValue={field.value}
                    >
                      <FormControl>
                        <SelectTrigger className="w-full bg-transparent dark:border-primary">
                          <SelectValue
                            className="text-primary"
                            placeholder="Select coin name"
                          />
                        </SelectTrigger>
                      </FormControl>
                      <SelectContent>
                        <SelectGroup>
                          <SelectItem value="bitcoin">Bitcoin</SelectItem>
                          <SelectItem value="ethereum">Ethereum</SelectItem>
                          <SelectItem value="usdt">USDT</SelectItem>
                          <SelectItem value="dodge">Dodge</SelectItem>
<<<<<<< HEAD
                          <SelectItem value="bnb">BNB</SelectItem>
=======
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
                        </SelectGroup>
                      </SelectContent>
                    </Select>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="amount"
                render={({ field }) => (
                  <FormItem className="space-y-4">
                    <FormLabel className="font-normal flex justify-between">
                      <span>Amount</span>{" "}
<<<<<<< HEAD
                      <span className="text-primary font-semibold ">
                        <ScrollArea className="w-36 h-5 items-center whitespace-nowrap rounded-md">
                          <div className="w-fit space-x-8 p-0">
                            {coinlist.map((coin) => (
                              <span
                                key={coin.id}
                                className="flex-1 text-muted-foreground overflow-hidden "
                              >
                                {coin.name} : {coin.sell_rate}
                              </span>
                            ))}
                          </div>
                          <ScrollBar orientation="horizontal" />
                        </ScrollArea>
=======
                      <span className="text-muted-foreground">
                        Rate: {OFFICIAL_RATES} / %
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
                      </span>
                    </FormLabel>
                    <FormControl>
                      <Input
                        className="bg-transparent border border-white"
                        type="number"
                        {...field}
                      />
                    </FormControl>
                    <FormDescription className="flex justify-between">
                      <span className="font-normal text-primary">
                        Amount: 0.0
                      </span>
                      <span className="text-[#4168B7] dark:text-[#A77700] font-normal flex items-center">
                        Set by Naira{" "}
                        <ArrowSwapHorizontal className="ml-2 w-6 h-6" />
                      </span>
                    </FormDescription>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="bankName"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel className="font-normal text-primary text-base">
<<<<<<< HEAD
                      Payment Name
=======
                      Bank Name
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
                    </FormLabel>
                    <Input
                      className="text-primary text-left font-medium dark:border-primary bg-transparent"
                      {...field}
                    />
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="accountNumber"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel className="font-normal text-primary text-base">
                      Account Number
                    </FormLabel>
                    <Input
                      className="text-primary text-left font-medium dark:border-primary bg-transparent"
                      {...field}
                    />
                    <FormMessage />
                  </FormItem>
                )}
              />
              <Button type="submit" variant="custom" className="w-full">
                Continue <BitcoinRefresh className="ml-2" />
              </Button>
            </form>
          </Form>
        </CardContent>
      </Card>
    </div>
  );
};

<<<<<<< HEAD
export default isAuth(Sellpage);
=======
export default Sellpage;
>>>>>>> c387ba2d01e1448e23ea9c21517a1ee2bd593f5c
